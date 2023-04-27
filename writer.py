import typing

import bitstring

from gif_objects import Gif


def write_gif(gif:Gif, io: typing.BinaryIO) -> None:
    gif_stream = bitstring.BitStream(b'')
    gif_stream