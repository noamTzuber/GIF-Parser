import binascii
import math
import typing

from PIL import Image as Image_PIL
from bitstring import ConstBitStream

from enums import BlockPrefix
from gif_objects import Gif, GraphicControlExtension, Image
from lzw import decode_lzw
from utils import bytes_to_int, int_to_bits, bits_to_int


def decode_gif(gif_stream: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object = Gif()
    decode_header(gif_stream, gif_object)
    decode_logical_screen_descriptor(gif_stream, gif_object)

    # There is no global color table if the size is 0.
    if gif_object.global_color_table_size != 0:
        decode_global_color_table(gif_stream, gif_object)

    while True:

        # Read the first byte to check if the next block is extension or image descriptor.
        extension_introducer = gif_stream.read(1)
        prefix = BlockPrefix(extension_introducer)

        if prefix is BlockPrefix.Extension:

            # Check which type of extension is the next block.
            extension_label = gif_stream.read(1)
            prefix = BlockPrefix(extension_label)

            if prefix is BlockPrefix.ApplicationExtension:
                decode_application_extension(gif_stream, gif_object)

            elif prefix is BlockPrefix.GraphicControlExtension:
                decode_graphic_control_extension(gif_stream, gif_object)

            elif prefix is BlockPrefix.CommentExtension:
                decode_comment_extension(gif_stream, gif_object)

            elif prefix is BlockPrefix.PlainTextExtension:
                decode_plain_text(gif_stream, gif_object)

        elif prefix is BlockPrefix.ImageDescriptor:

            # Creat a new Image object and add it to the end of the image array in the Gif.
            gif_object.images.append(Image())
            decode_image_descriptor(gif_stream, gif_object)

            # Check if there is a Local color table for this image.
            if gif_object.images[-1].local_color_table_flag == 1:
                decode_local_color_table(gif_stream, gif_object)

            decode_image_data(gif_stream, gif_object)
        elif prefix is BlockPrefix.NONE:
            break

    return gif_object


def decode_header(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode the header of the file"""
    block = gif_stream.read(6)
    gif_object.version = block.decode()


def decode_logical_screen_descriptor(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode logical screen descriptor"""
    block: bytes = gif_stream.read(7)

    gif_object.width = bytes_to_int(block, start=0, size=2)
    gif_object.height = bytes_to_int(block, start=2, size=2)

    packed_int: int = block[4]
    packed_bits: str = int_to_bits(packed_int)

    global_color_table_exist = bits_to_int(packed_bits, 0)
    if global_color_table_exist:
        gif_object.global_color_table_size = 3 * pow(2, bits_to_int(packed_bits, 5, 7) + 1)

    gif_object.resolution = bits_to_int(packed_bits, 1, 3)


def decode_global_color_table(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """
    Decode global color table.
    We read the number of bytes we received in the flag in Logical Screen Descriptor,
    and divided into triplets of bytes pairs, each triplet representing RGB of a color.
    """
    gif_object.global_color_table = [gif_stream.read(3) for i in range(
        int(gif_object.global_color_table_size / 3))]


def decode_application_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode global color table"""
    app_ex = ApplicationExtension()

    block_size = int.from_bytes(gif_stream.read(1), "little")

    app_ex.application_name = gif_stream.read(8).decode("utf-8")
    app_ex.identify = gif_stream.read(3).decode("utf-8")

    application_data = ""
    while (number_of_sub_block_bytes := gif_stream.read(1)) != b'\x00':
        sub_block = gif_stream.read(int.from_bytes(number_of_sub_block_bytes, "little")).decode("utf-8")
        application_data +=sub_block

    app_ex.information = application_data
    gif_object.add_application_extension(app_ex)


def decode_graphic_control_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode graphic control extension"""

    # Create new Graphic Control Extensions and append it to the list in the Gif object.
    gif_object.graphic_control_extensions.append(GraphicControlExtension())
    block: bytes = gif_stream.read(6)

    packed_int: int = block[1]
    packed_bits: str = int_to_bits(packed_int)

    # Get the flags from the packed bits.
    gif_object.graphic_control_extensions[-1].disposal = bits_to_int(packed_bits, 3, 3)
    gif_object.graphic_control_extensions[-1].user_input_flag = bits_to_int(packed_bits, 6, 1)

    gif_object.graphic_control_extensions[-1].delay_time = bytes_to_int(block, start=2, size=2)
    gif_object.graphic_control_extensions[-1].transparent_flag = bytes_to_int(block, start=4, size=1)


def decode_image_descriptor(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode image descriptor"""
    # before getting in we create image and add it to the gif anf the gif will send to this function
    # and add the last gce to this image

    current_image = gif_object.images[-1]

    current_image.left = int.from_bytes(gif_stream.read(2), "little")
    current_image.top = int.from_bytes(gif_stream.read(2), "little")
    current_image.width = int.from_bytes(gif_stream.read(2), "little")
    current_image.height = int.from_bytes(gif_stream.read(2), "little")

    stream = ConstBitStream(gif_stream.read(1))

    current_image.local_color_table_flag = stream.read('bin1')
    current_image.interlace_flag = stream.read('bin1')

    # those attributes are not necessary for the gif
    current_image.sort_flag = int(stream.read('bin1'), 2)
    # we don't need it - reading just for moving the pos forward
    reserved_for_future_use = int(stream.read('bin2'), 2)
    current_image.size_of_local_color_table = int(stream.read('bin3'), 2)


def decode_local_color_table(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    current_image = gif_object.images[-1]
    size_of_color_table = math.pow(2, current_image.size_of_local_color_table + 1)

    colors_array = [gif_stream.read(3) for i in range(int(size_of_color_table))]
    gif_object.local_color_tables.append(colors_array)
    current_image.local_color_table_index = len(gif_object.local_color_tables) - 1


def decode_image_data(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode image data"""
    bytes_image_data = b''
    current_image = gif_object.images[-1]

    lzw_minimum_code_size = int.from_bytes(gif_stream.read(1), "little")
    index_length = math.ceil(math.log(lzw_minimum_code_size + 1)) + 1

    while (number_of_sub_block_bytes := gif_stream.read(1)) != b'\x00':
        compressed_sub_block = (gif_stream.read(int.from_bytes(number_of_sub_block_bytes, "little"))).hex()
        res = decode_lzw(compressed_sub_block, math.pow(2, lzw_minimum_code_size))
        bytes_image_data += res

    if current_image.local_color_table_flag == 1:
        local_color_table = gif_object.local_color_tables[-1]
    else:
        local_color_table = gif_object.global_color_table

    for pos in range(0, len(bytes_image_data), index_length):
        current_index = int((bytes_image_data[pos:pos + index_length]), 2)
        # save the index
        current_image.image_indexes.append(current_index)
        # convert index to rgb
        current_image.image_data.append(local_color_table[current_index])

    current_image.img = create_img(current_image.image_data, current_image.width, current_image.height)


def create_img(image_data: list[str], width: int, height: int) -> Image_PIL:
    # Create a new image with the specified size
    img = Image_PIL.new('RGB', (width, height))

    rgb_array = ["#" + binascii.hexlify(b).decode('utf-8').upper() for b in image_data]

    # Set the pixel values of the image using the RGB array
    pixels = img.load()
    # for each pixel - we take specific color ("#FF0000") and diveide it to 3 parts("FF","00","00") of RGB.
    # then convert it from hex(16) to int (255,0,0), in the end we get tuple of three numbers that represent the color
    for i in range(width):
        for j in range(height):
            pixels[i, j] = tuple(int(rgb_array[j * width + i][k:k + 2], 16) for k in (1, 3, 5))
    img.show()
    return img


def decode_comment_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode comment extension"""
    raise NotImplemented


def decode_plain_text(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode plain text"""
    raise NotImplemented
