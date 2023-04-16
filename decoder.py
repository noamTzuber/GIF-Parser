import binascii
import math
import typing

from PIL import Image as Image_PIL
import bitstring

from bitstream import BitStream
from enums import BlockPrefix
from gif_objects import Gif, GraphicControlExtension, Image, ApplicationExtension
from lzw import decode_lzw
from utils import bytes_to_int, int_to_bits, bits_to_int


def decode_gif(io: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object: Gif = Gif()
    gif_stream: BitStream = BitStream(bitstring.ConstBitStream(io))

    decode_header(gif_stream, gif_object)
    decode_logical_screen_descriptor(gif_stream, gif_object)

    # There is no global color table if the size is 0.
    if gif_object.global_color_table_size != 0:
        decode_global_color_table(gif_stream, gif_object)

    while True:

        # Read the first byte to check if the next block is extension or image descriptor.
        extension_introducer: bytes = gif_stream.read(1)
        prefix = BlockPrefix(extension_introducer)

        if prefix is BlockPrefix.Extension:

            # Check which type of extension is the next block.
            extension_label: bytes = gif_stream.read(1)
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


def decode_header(gif_stream: BitStream, gif_object: Gif) -> None:
    block = gif_stream.read_bytes(6)
    gif_object.version = block.decode()


def decode_logical_screen_descriptor(gif_stream: BitStream, gif_object: Gif) -> None:
    gif_object.width = gif_stream.read_unsigned_integer(2, 'bytes')
    gif_object.height = gif_stream.read_unsigned_integer(2, 'bytes')

    global_color_table_exist = gif_stream.read_bool()

    gif_object.resolution = gif_stream.read_unsigned_integer(3, 'bits')

    is_ordered = gif_stream.read_bool()

    global_color_table_size_value = gif_stream.read_unsigned_integer(3, 'bits')
    if global_color_table_exist:
        gif_object.global_color_table_size = 3 * pow(2, global_color_table_size_value + 1)
    else:
        gif_object.global_color_table_size = 0

    transperent_index = gif_stream.read_unsigned_integer(1, 'bytes')

    pixel_ratio_value = gif_stream.read_unsigned_integer(1, 'bytes')
    pixel_ratio = (pixel_ratio_value + 15) / 64


def decode_global_color_table(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """
    Decode global color table.
    We read the number of bytes we received in the flag in Logical Screen Descriptor,
    and divided into triplets of bytes pairs, each triplet representing RGB of a color.
    """
    gif_object.global_color_table = [gif_stream.read(3) for i in range(
        int(gif_object.global_color_table_size / 3))]


def decode_application_extension(gif_stream: BitStream, gif_object: Gif) -> None:
    app_ex = ApplicationExtension()

    block_size = gif_stream.read_unsigned_integer(1, 'bytes')
    if block_size != 12:
        # raise Exception("incorrect file format")
        pass

    app_ex.application_name = gif_stream.read_bytes(8).decode("utf-8")
    app_ex.identify = gif_stream.read_bytes(3).decode("utf-8")

    application_data = ""
    while (number_of_sub_block_bytes := gif_stream.read_unsigned_integer(1, 'bytes')) != 0:
        sub_block = gif_stream.read_bytes(number_of_sub_block_bytes).decode("utf-8")
        application_data += sub_block

    app_ex.information = application_data
    gif_object.add_application_extension(app_ex)

    block_terminator = gif_stream.read_bytes(1)
    if block_terminator != '\x00':
        # raise Exception("incorrect file format")
        pass


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


def decode_image_descriptor(gif_stream: BitStream, gif_object: Gif) -> None:
    # before getting in we create image and add it to the gif anf the gif will send to this function
    # and add the last gce to this image

    current_image = gif_object.images[-1]

    current_image.left = gif_stream.read_unsigned_integer(2, 'bytes')
    current_image.top = gif_stream.read_unsigned_integer(2, 'bytes')
    current_image.width = gif_stream.read_unsigned_integer(2, 'bytes')
    current_image.height = gif_stream.read_unsigned_integer(2, 'bytes')

    current_image.local_color_table_flag = gif_stream.read_bool()
    current_image.interlace_flag = gif_stream.read_bool()

    # those attributes are not necessary for the gif
    current_image.sort_flag = gif_stream.read_bool()

    # skipping 2 bits
    gif_stream.skip(2, 'bits')

    current_image.size_of_local_color_table = gif_stream.read_unsigned_integer(3, 'bits')


def decode_local_color_table(gif_stream: BitStream, gif_object: Gif) -> None:
    current_image = gif_object.images[-1]
    size_of_color_table = math.pow(2, current_image.size_of_local_color_table + 1)

    colors_array = [gif_stream.read_bytes(3) for _ in range(int(size_of_color_table))]
    gif_object.local_color_tables.append(colors_array)
    current_image.local_color_table_index = len(gif_object.local_color_tables) - 1


def decode_image_data(gif_stream: BitStream, gif_object: Gif) -> None:
    current_image = gif_object.images[-1]

    lzw_minimum_code_size = gif_stream.read_unsigned_integer(1, 'bytes')
    index_length = math.ceil(math.log(lzw_minimum_code_size + 1)) + 1

    bytes_image_data = b''
    while (number_of_sub_block_bytes := gif_stream.read_unsigned_integer(1, 'bytes')) != 0:
        compressed_sub_block = gif_stream.read_hex(number_of_sub_block_bytes, 'bytes')
        res = decode_lzw(compressed_sub_block, math.pow(2, lzw_minimum_code_size))
        bytes_image_data += res

    if current_image.local_color_table_flag:
        local_color_table = gif_object.local_color_tables[-1]
    else:
        local_color_table = gif_object.global_color_table

    for pos in range(0, len(bytes_image_data), index_length):
        current_index = int(bytes_image_data[pos:pos + index_length], 2)
        # save the index
        current_image.image_indexes.append(current_index)
        # convert index to rgb
        current_image.image_data.append(local_color_table[current_index])

    current_image.img = create_img(current_image.image_data, current_image.width, current_image.height)


def create_img(image_data: list[str], width: int, height: int) -> Image_PIL:
    # can be replaced with ""
    Image_PIL.frombytes('RGB', (width, height), b''.join(image_data)).show()
    # Create a new image with the specified size
    img = Image_PIL.new('RGB', (width, height))
    rgb_array = ["#" + binascii.hexlify(b).decode('utf-8').upper() for b in image_data]

    # Set the pixel values of the image using the RGB array
    pixels = img.load()

    # for each pixel - we take specific color ("#FF0000") and divide it to 3 parts("FF","00","00") of RGB.
    # then convert it from hex(16) to int (255,0,0), in the end we get tuple of three numbers that represent the color
    # The code iterates over each pixel in an image represented as a two-dimensional array of hex color codes.
    # It then extracts the red, green, and blue color components of each pixel by converting the hex codes to integers
    # and stores them as a tuple of three integers
    for row in range(width):
        for column in range(height):
            hex_color = rgb_array[column * width + row]
            r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
            pixels[row, column] = (r, g, b)

    return img


def decode_comment_extension(gif_stream: ConstBitStream, gif_object: Gif) -> None:
    """decode comment extension"""
    data = ''
    # every sub block start with a bye that present the size of it.
    sub_block_size = gif_stream.read("uint:8")
    while sub_block_size != 0:  # Change to Block Terminator enum
        size_in_bits = 8 * sub_block_size
        data += gif_stream.read(f"uintle:{size_in_bits}")
        sub_block_size = gif_stream.read("uint:8")


def decode_plain_text(gif_stream: ConstBitStream, gif_object: Gif) -> None:
    """decode plain text"""

    # Read the block size (always 12)
    gif_stream.read("uint:8")
    gif_object.plain_text_extensions[-1].left = gif_stream.read("uintle:16")
    gif_object.plain_text_extensions[-1].top = gif_stream.read("uintle:16")
    gif_object.plain_text_extensions[-1].width = gif_stream.read("uintle:16")
    gif_object.plain_text_extensions[-1].height = gif_stream.read("uintle:16")
    gif_object.plain_text_extensions[-1].char_width = gif_stream.read("uint:8")
    gif_object.plain_text_extensions[-1].char_height = gif_stream.read("uint:8")
    gif_object.plain_text_extensions[-1].text_color = gif_stream.read("uint:8")
    gif_object.plain_text_extensions[-1].background_color = gif_stream.read("uint:8")

    data = ''
    # every data sub block start with a bye that present the size of it.
    sub_block_size = gif_stream.read("uint:8")
    while sub_block_size != 0:  # Change to Block Terminator enum
        size_in_bits = 8 * sub_block_size
        data += gif_stream.read(f"uintle:{size_in_bits}")
        sub_block_size = gif_stream.read("uint:8")

    gif_object.plain_text_extensions[-1].text_data = data