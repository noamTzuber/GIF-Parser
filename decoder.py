import typing

from classes import Gif


def decode(gif: typing.BinaryIO) -> Gif:
    """decodes the file using support functions below"""
    gif_object = Gif()
    # TODO: add decode logic
    raise NotImplemented
    return gif_object


def get_bits(byte, start, end=None):
    """given byte, returns the bits at the specified locations"""
    raise NotImplemented


def read_header(gif: typing.BinaryIO, gif_object: Gif):
    """reads the header of the file"""
    gif.version = gif.read(6)


def read_LSD(gif: typing.BinaryIO, gif_object: Gif):
    """reads logical screen descriptor"""
    block = gif.read(7)
    LSD = {}
    packed = {}
    gif_object.width = block[0:1]
    gif_object.height = block[2:3]
    packedBytes = block[4]
    gif_object.GCT
    packed['GCTFlag'] = get_bits(packedBytes, 0)
    packed['colorResolution'] = get_bits(packedBytes, 1, 3)
    packed['sortFlag'] = get_bits(packedBytes, 4)
    packed['sizeOfGCT'] = get_bits(packedBytes, 5, 7)
    LSD['packed'] = packed
    LSD['backgroundColor'] = block[5]
    LSD['pixelAspectRatio'] = block[6]
    gif_object["LSD"] = LSD


def read_GCT(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_Application_Extension(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_Graphic_Control_Extension(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def image_descriptor(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_local_color_table(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_image_data(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_comment_extension(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented


def read_plain_text(gif: typing.BinaryIO, gif_object: Gif):
    raise NotImplemented
