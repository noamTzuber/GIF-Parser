import math

from PIL import Image as Image_PIL

from bitstream import BitStream
from bitstream_writer import BitStreamWriter
from gif_objects import Gif


def write_gif(gif_object: Gif) -> BitStreamWriter:
    gif_stream = BitStreamWriter()

    write_header(gif_stream, gif_object)
    write_logical_screen_descriptor(gif_stream, gif_object)

    if gif_object.global_color_table_size != 0:
        write_logical_screen_descriptor(gif_stream, gif_object)

    # TODO: continue writing

    return gif_stream


def write_header(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    bytes = gif_object.version.encode()
    gif_stream.write_bytes(bytes)


def write_logical_screen_descriptor(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    gif_stream.write_unsigned_integer(gif_object.width, 2, 'bytes')
    gif_stream.write_unsigned_integer(gif_object.height, 2, 'bytes')

    # if global color table exist
    global_color_table_exist = gif_object.global_color_table_size != 0
    gif_stream.write_bool(global_color_table_exist)

    # both not relevant
    gif_stream.write_unsigned_integer(gif_object.color_resolution, 3, 'bits')
    gif_stream.write_bool(gif_object.sort_flag)

    global_color_table_size_value = int(math.log2(gif_object.global_color_table_size)) - 1
    if global_color_table_exist:
        gif_stream.write_unsigned_integer(global_color_table_size_value, 3, 'bits')
    else:
        gif_stream.write_unsigned_integer(0, 3, 'bits')

    gif_stream.write_unsigned_integer(gif_object.background_color_index, 1, 'bytes')

    pixel_ratio_value = int(gif_object.pixel_aspect_ratio * 64 - 15)
    gif_stream.write_unsigned_integer(pixel_ratio_value, 1, 'bytes')


def write_global_color_table(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    raise NotImplemented


def write_application_extension(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    application_ex = gif_object.applications_extensions[-1]
    gif_stream.write_bytes(Extension)
    gif_stream.write_bytes(ApplicationExtension)
    gif_stream.write_unsigned_integer(ApplicationExtensionBlockSize, 1, 'bytes')

    gif_stream.write_bytes(application_ex.application_name)
    gif_stream.write_bytes(application_ex.identify)

    # split the data into group of 255 bytes, evert byte present as two char
    # so every sub block should be 510
    sub_blocks = [(application_ex.data[i:i + 510]) for i in range(0, len(string), 255)]

    for sub_block in sub_blocks:
        sub_block_size = len(sub_block)
        gif_stream.write_bytes(sub_block_size)
        gif_stream.write_bytes(sub_block)

    gif_stream.write_bytes(BlockTerminator)


def write_graphic_control_extension(gif_stream: BitStreamWriter, gif_object: Gif) -> None:
    graphic_control_ex = gif_object.graphic_control_extensions[-1]
    gif_stream.write_bytes(Extension)
    gif_stream.write_bytes(GraphicControlExtension)

    gif_stream.write_unsigned_integer(GraphicControlExtensionBlockSize, 1, 'bytes')

    # write package
    gif_stream.write_unsigned_integer(graphic_control_ex.reserved, 3, 'bits')
    gif_stream.write_unsigned_integer(graphic_control_ex.disposal, 3, 'bits')
    gif_stream.write_bool(graphic_control_ex.disposaluser_input_flag)
    gif_stream.write_unsigned_integer(graphic_control_ex.transparent_color_flag, 1, 'bits')

    gif_stream.write_unsigned_integer(graphic_control_ex.delay_time, 2, 'bytes')
    gif_stream.write_unsigned_integer(graphic_control_ex.transparent_index, 1, 'bytes')

    gif_stream.write_bytes(BlockTerminator)


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
