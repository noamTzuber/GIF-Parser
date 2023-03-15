import typing

from classes import Gif


def decode(gif: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object = Gif()
    # TODO: add decode logic
    raise NotImplemented
    return gif_object


def get_bits(byte, start, end=None) -> int:
    """given byte, returns the int representation of the bits at the specified locations including start and end"""
    raise NotImplemented


def decode_header(gif: typing.BinaryIO, gif_object: Gif) -> None:
    """reads the header of the file"""
    gif_object.version = gif.read(6)


def decode_logical_screen_descriptor(gif: typing.BinaryIO, gif_object: Gif) -> None:
    """reads logical screen descriptor"""
    block = gif.read(7)

    gif_object.width = block[0:1]
    gif_object.height = block[2:3]

    packed_bytes = block[4]

    global_color_table_exist = get_bits(packed_bytes, 0)
    if global_color_table_exist:
        gif_object.global_color_table_size = get_bits(packed_bytes, 5, 7)

    gif_object.resolution = get_bits(packed_bytes, 1, 3)


def decode_global_color_table(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_application_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_graphic_control_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_image_descriptor(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_local_color_table(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_image_data(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_comment_extension(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented


def decode_plain_text(gif: typing.BinaryIO, gif_object: Gif) -> None:
    raise NotImplemented
