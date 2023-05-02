import typing
from pprint import pprint

from PIL import Image as Image_PIL
from attrs import define, field
from deepdiff import DeepDiff


class IncorrectFileFormat(Exception):
    def __init__(self, message):
        super().__init__(message)


class DifferentClasses(Exception):
    def __init__(self, message):
        super().__init__(message)


class Differentiable:
    def diff(self, other):
        if type(self) != type(other):
            raise DifferentClasses(f"different classes, this: {type(self)}, other: {type(other)}")
        return DeepDiff(self, other)

    def print_diff(self, other):
        pprint(self.diff(other))


@define
class ApplicationExtension(Differentiable):
    application_name: str = None
    identify: str = None
    data: str = None


@define
class GraphicControlExtension(Differentiable):
    disposal: int = field(default=None)
    reserved: int = field(default=None)
    user_input_flag: bool = field(default=None)
    transparent_color_flag: int = field(default=None)
    transparent_index: int = field(default=None)
    delay_time: int = field(default=None)


@define
class PlainTextExtension(Differentiable):
    top: int = field(default=None)
    left: int = field(default=None)
    width: int = field(default=None)
    height: int = field(default=None)

    char_width: int = field(default=None)
    char_height: int = field(default=None)
    background_color: int = field(default=None)
    text_color: str = field(default=None)
    text_data: str = field(default=None)


@define
class CommentExtension:
    data: int = field(default=None)


@define
class Image(Differentiable):
    image_data: list[typing.Any] = field(factory=list, repr=False)
    image_indexes: list[typing.Any] = field(factory=list, repr=False)

    top: int = field(default=None)
    left: int = field(default=None)
    width: int = field(default=None)
    height: int = field(default=None)

    interlace_index: int = field(default=None)
    sort_flag: bool = field(default=None)
    reserved: int = field(default=None)
    local_color_table_flag: bool = field(default=None)
    background_color_index: int = field(default=None)
    size_of_local_color_table: int = field(default=None)

    # we think we don't need it
    img: Image_PIL.Image = field(default=None)


@define
class Gif(Differentiable):
    structure: list[typing.Any]
    images: list[Image] = field(factory=list, repr=False)
    applications_extensions: list[ApplicationExtension] = field(factory=list, repr=False)
    comments_extensions: list[CommentExtension] = field(factory=list, repr=False)
    graphic_control_extensions: list[GraphicControlExtension] = field(factory=list, repr=False)
    plain_text_extensions: list[PlainTextExtension] = field(factory=list, repr=False)
    local_color_tables: list[list[bytes]] = field(factory=list, repr=False)

    version: str = field(default=None)
    width: int = field(default=None)
    height: int = field(default=None)

    global_color_table_size: int = field(default=None)
    color_resolution: int = field(default=None)
    sort_flag: bool = field(default=None)
    global_color_table: Image_PIL.Image = field(default=None, repr=False)
    background_color_index: int = field(default=None)
    pixel_aspect_ratio: int = field(default=None)

    def add_application_extension(self, extension):
        self.applications_extensions.append(extension)
