from PIL import Image as Image_PIL

from bitstream import BitStream
from bitstream_writer import BitStreamWriter
from gif_objects import Gif


def write_gif(gif_object: Gif) -> None:
    gif_stream = BitStreamWriter()

    write_header(gif_stream, gif_object)
    write_logical_screen_descriptor(gif_stream, gif_object)

    if gif_object.global_color_table_size != 0:
        write_logical_screen_descriptor(gif_stream, gif_object)

    # TODO: continue writing


def write_header(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_logical_screen_descriptor(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_global_color_table(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_application_extension(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_graphic_control_extension(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_image_descriptor(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_local_color_table(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_image_data(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def create_img(image_data: list[str], width: int, height: int) -> Image_PIL:
    raise NotImplemented


def write_comment_extension(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_plain_text(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented
