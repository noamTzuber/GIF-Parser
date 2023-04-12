from PIL import Image as Image_PIL


class Gif:
    def __init__(self):
        self._version: str = None
        self._width: int = None
        self._height: int = None
        self._resolution: int = None
        self._global_color_table_size: int = None
        self._global_color_table = None
        self._images: list[Image] = []
        self._applications_extensions: list[ApplicationExtension] = []
        self._graphic_control_extensions: list[GraphicControlExtension] = []
        self._local_color_tables = []

    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def resolution(self) -> int:
        return self._resolution

    @resolution.setter
    def resolution(self, value: int):
        self._resolution = value

    @property
    def global_color_table_size(self) -> int:
        return self._global_color_table_size

    @global_color_table_size.setter
    def global_color_table_size(self, value: int):
        self._global_color_table_size = value

    @property
    def global_color_table(self):
        return self._global_color_table

    @global_color_table.setter
    def global_color_table(self, value):
        self._global_color_table = value

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value

    @property
    def comments_extension(self):
        return self._comments_extension

    @comments_extension.setter
    def comments_extension(self, value):
        self._comments_extension = value

    @property
    def applications_extension(self):
        return self._applications_extensions

    @applications_extension.setter
    def applications_extension(self, value):
        self._applications_extensions = value

    def add_application_extension(self, extension):
        self._applications_extensions.append(extension)

    @property
    def graphic_control_extensions(self):
        return self._graphic_control_extensions

    @graphic_control_extensions.setter
    def graphic_control_extensions(self, value):
        self._graphic_control_extensions = value

    @property
    def local_color_tables(self):
        return self._local_color_tables

    @local_color_tables.setter
    def local_color_tables(self, value):
        self._local_color_tables = value


class ApplicationExtension:
    def __init__(self):
        self._application_name: str = None
        self._identify: str = None
        self._data: str = None

    @property
    def application_name(self) -> str:
        return self._application_name

    @application_name.setter
    def application_name(self, name: str):
        self._application_name = name

    @property
    def identify(self) -> str:
        return self._identify

    @identify.setter
    def identify(self, identify: str):
        self._identify = identify

    @property
    def information(self) -> str:
        return self._data

    @information.setter
    def information(self, data: str):
        self._data = data


class GraphicControlExtension:
    def __init__(self):
        self._disposal: int = None
        self._user_input_flag: int = None
        self._transparent_flag: int = None
        self._delay_time: int = None

    @property
    def disposal(self) -> int:
        return self._disposal

    @disposal.setter
    def disposal(self, value: int):
        self._disposal = value

    @property
    def user_input_flag(self) -> int:
        return self._user_input_flag

    @user_input_flag.setter
    def user_input_flag(self, value: int):
        self._user_input_flag = value

    @property
    def transparent_flag(self) -> int:
        return self._transparent_flag

    @transparent_flag.setter
    def transparent_flag(self, value: int):
        self._transparent_flag = value

    @property
    def delay_time(self) -> int:
        return self._delay_time

    @delay_time.setter
    def delay_time(self, value: int):
        self._delay_time = value


class PlainTextExtension:
    def __init__(self):
        self._top: int = None
        self._left: int = None
        self._width: int = None
        self._height: int = None
        self._char_width: int = None
        self._char_height: int = None
        self._background_color = None
        self._text_color = None
        self._text_data: str = None

    @property
    def top(self) -> int:
        return self._top

    @top.setter
    def top(self, value: int):
        self._top = value

    @property
    def left(self) -> int:
        return self._left

    @left.setter
    def left(self, value: int):
        self._left = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def char_width(self) -> int:
        return self._char_width

    @char_width.setter
    def char_width(self, value: int):
        self._char_width = value

    @property
    def char_height(self) -> int:
        return self._char_height

    @char_height.setter
    def char_height(self, value: int):
        self._char_height = value

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = value

    @property
    def text_data(self) -> str:
        return self._text_data

    @text_data.setter
    def text_data(self, value: str):
        self._text_data = value


class Image:
    def __init__(self):
        self._top: int = None
        self._left: int = None
        self._width: int = None
        self._height: int = None
        self._interlace_flag: int = None
        self._graphic_control_extension_index: int = None
        self._image_data = []
        self._image_indexes = []
        # we think we dont need it
        self._local_color_table_index: int = None
        self._plain_text_extension_index: int = None
        self._img = None

    @property
    def top(self) -> int:
        return self._top

    @top.setter
    def top(self, value: int):
        self._top = value

    @property
    def left(self) -> int:
        return self._left

    @left.setter
    def left(self, value: int):
        self._left = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def interlace_flag(self) -> int:
        return self._interlace_flag

    @interlace_flag.setter
    def interlace_flag(self, value: int):
        self._interlace_flag = value

    @property
    def graphic_control_extension_index(self) -> int:
        return self._graphic_control_extension_index

    @graphic_control_extension_index.setter
    def graphic_control_extension_index(self, value: int):
        self._graphic_control_extension_index = value

    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, value):
        self._image_data = value

    @property
    def image_indexes(self):
        return self._image_indexes

    @image_indexes.setter
    def image_indexes(self, value):
        self._image_indexes = value

    @property
    def local_color_table_index(self) -> int:
        return self._local_color_table_index

    @local_color_table_index.setter
    def local_color_table_index(self, value: int):
        self._local_color_table_index = value

    @property
    def plain_text_extension_index(self) -> int:
        return self._plain_text_extension_index

    @plain_text_extension_index.setter
    def plain_text_extension_index(self, value: int):
        self._plain_text_extension_index = value

    @property
    def img(self) -> Image_PIL:
        return self._img

    @img.setter
    def img(self, value: Image_PIL):
        self._img = value
