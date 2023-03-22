import math
import typing

from bitstring import ConstBitStream

from gif_objects import Gif
from lzw import decode_lzw


def decode_gif(gif_stream: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object = Gif()
    # TODO: add decode logic
    decode_header(gif_stream, gif_object)
    decode_logical_screen_descriptor(gif_stream, gif_object)

    return gif_object


def int_to_bits(num: int) -> str:
    """
    given int, returns the bits representation of the int as string without prefix
    example: int_to_bits(11) = '1011'
    """
    return bin(num).removeprefix('0b')


def bits_to_int(bits: str, start: int = 0, size: int = 1) -> int:
    """
    given byte, returns the int representation of the bits from start and size amount
    example: bits_to_int('1011', 2, 2) = 3
        because, the bits from index 2 and 2 bits are '11' and is 3 in binary
    """
    end: int = start + size
    return int(bits[start:end], 2)


def bytes_to_int(block: bytes, start: int = 0, size: int = 1) -> int:
    """
    given bytes, returns the int representation of the bytes from start and size
    example: bytes_to_int(b'\n\x00\n\x00\x91\x00\x00', 2, 2) = 10
        because, the 2 bytes from index 2 are b'\n\x00\' which are 10 in little endian
    """
    end: int = start + size
    return int.from_bytes(block[start:end], "little", signed=False)


def single_byte(block: bytes, index: int) -> bytes:
    """
    given bytes array, returns a single byte at specific location
    example: single_byte(b'\n\x00\n\x00\x91\x00\x00', 2) = b'\n'
    """
    end: int = index + 1
    return block[index:end]


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
        gif_object.global_color_table_size = bits_to_int(packed_bits, 5, 7)

    gif_object.resolution = bits_to_int(packed_bits, 1, 3)


def decode_global_color_table(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode global color table"""
    raise NotImplemented


def decode_application_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode global color table"""
    raise NotImplemented


def decode_graphic_control_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode graphic control extension"""
    raise NotImplemented


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
    current_image.sort_flag = int.from_bytes(stream.read('bin1'), "little")
    # we don't need it - reading just for moving the pos forward
    reserved_for_future_use = stream.read('bin2')
    current_image.size_of_local_color_table = int.from_bytes(stream.read('bin3'), "little")


def decode_local_color_table(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    # current_image = gif_object.images[-1]
    # size_of_color_table = math.pow(2, current_image.size_of_local_color_table + 1)
    size_of_color_table = 4

    colors_array = [gif_stream.read(3) for i in range(int(size_of_color_table))]


def decode_image_data(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode image data"""
    bytes_image_data = b''
    # current_image = gif_object.images[-1]

    lzw_minimum_code_size = int.from_bytes(gif_stream.read(1), "little")
    index_length = math.ceil(math.log(lzw_minimum_code_size + 1)) + 1

    while (number_of_sub_block_bytes := gif_stream.read(1)) != b'\x00':
        """check the number of the reading bytes"""
        compressed_sub_block = (gif_stream.read(int.from_bytes(number_of_sub_block_bytes, "little"))).hex()
        bytes_image_data += decode_lzw(compressed_sub_block, math.pow(2, lzw_minimum_code_size))

    # local_color_table = gif_object.LCTs[-1]

    # pos = 0
    # for i in range(int(len(bytes_image_data) / index_length)):
    #     current_image.image_data.append(local_color_table[bytes_image_data[pos:pos + index_length]])
    #     pos += index_length


def decode_comment_extension(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode comment extension"""
    raise NotImplemented


def decode_plain_text(gif_stream: typing.BinaryIO, gif_object: Gif) -> None:
    """decode plain text"""
    raise NotImplemented
