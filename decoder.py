import typing

from bitstring import ConstBitStream

from classes import Gif


def decode(gif: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object = Gif()
    # TODO: add decode logic
    decode_header(gif, gif_object)
    decode_logical_screen_descriptor(gif, gif_object)
    return gif_object


def int_to_bits(num: int) -> str:
    """given byte, returns the int representation of the bits at the specified locations including start"""
    return bin(num).removeprefix('0b')


def bits_to_int(bits: str, start: int, amount: int = 1) -> int:
    """given byte, returns the int representation of the bits at the specified locations including start"""
    end: int = start + amount
    return int(bits[start:end], 2)


def bytes_to_int(block: bytes, start: int = 0, amount: int = 1) -> int:
    """given bytes, returns the int representation of the bytes"""
    end: int = start + amount
    return int.from_bytes(block[start:end], "little", signed=False)


def single_byte(block: bytes, index: int) -> bytes:
    """given bytes, returns the int representation of the bytes"""
    end: int = index + 1
    return block[index:end]


def decode_header(gif: typing.BinaryIO, gif_object: Gif) -> None:
    """reads the header of the file"""
    block = gif.read(6)
    gif_object.version = block.decode()


def decode_logical_screen_descriptor(gif: typing.BinaryIO, gif_object: Gif) -> None:
    """reads logical screen descriptor"""
    block: bytes = gif.read(7)

    gif_object.width = bytes_to_int(block, start=0, amount=2)
    gif_object.height = bytes_to_int(block, start=2, amount=2)

    packed_int: int = block[4]
    packed_bits: str = int_to_bits(packed_int)

    global_color_table_exist = bits_to_int(packed_bits, 0)
    if global_color_table_exist:
        gif_object.global_color_table_size = bits_to_int(packed_bits, 5, 7)

    gif_object.resolution = bits_to_int(packed_bits, 1, 3)


def decode_global_color_table(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_application_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_graphic_control_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_image_descriptor(gif: typing.BinaryIO, gif_object: Gif) -> None:
    # before getting in we create image and add it to the gif anf the gif will send to this function
    # and add the last gce to this image

    current_image = gif_object.images[-1]

    current_image.left = gif.read(2)
    current_image.top = gif.read(2)
    current_image.width = gif.read(2)
    current_image.height = gif.read(2)

    stream = ConstBitStream(gif.read(1))

    current_image.local_color_table_flag = stream.read('bin1')
    current_image.interlace_flag = stream.read('bin1')

    # those attributes are not necessary for the gif
    # sort_flag = stream.read('bin1')
    # reserved_for_future_use = stream.read('bin2')
    # size_of_local_color_table = stream.read('bin3')


def decode_local_color_table(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_image_data(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_comment_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_plain_text(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented
