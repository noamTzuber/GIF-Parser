import typing
from dataclasses import dataclass, field

from PIL import Image as Image_PIL


@dataclass(slots=True)
class ApplicationExtension:
    application_name: str = None
    identify: str = None
    data: str = None


@dataclass(slots=True)
class GraphicControlExtension:
    disposal: int = None
    user_input_flag: int = None
    transparent_flag: int = None
    delay_time: int = None


@dataclass(slots=True)
class PlainTextExtension:
    top: int = None
    left: int = None
    width: int = None
    height: int = None
    char_width: int = None
    char_height: int = None
    background_color = None
    text_color = None
    text_data: str = None


@dataclass(slots=True)
class Image:
    top: int = None
    left: int = None
    width: int = None
    height: int = None
    interlace_index: int = None
    local_color_table_flag: bool = False
    graphic_control_extension_index: int = None
    background_color_index: int = None
    image_data = []
    image_indexes = []
    # we think we don't need it
    local_color_table_index: int = None
    plain_text_extension_index: int = None
    img: Image_PIL = None


@dataclass(slots=True)
class Gif:
    version: str = None
    width: int = None
    height: int = None
    global_color_table_size: int = None
    global_color_table: Image_PIL = None
    images: list[Image] = field(default_factory=list)
    applications_extensions: list[ApplicationExtension] = field(default_factory=list)
    graphic_control_extensions: list[GraphicControlExtension] = field(default_factory=list)
    plain_text_extensions: list[PlainTextExtension] = field(default_factory=list)
    local_color_tables: list[Image_PIL] = field(default_factory=list)

    def add_application_extension(self, extension):
        self.applications_extensions.append(extension)


class IncorrectFileFormat(Exception):
    def __init__(self, message):
        super().__init__(message)
