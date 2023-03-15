class Gif:
    def __init__(self):
        self._version = None
        self._width = None
        self._height = None
        self._resolution = None
        self._global_color_table_size = None
        self._global_color_table = None
        self._images = []
        self._comments_extensions = []
        self._applications_extensions = []
        self._graphic_control_extensions = []
        self._local_color_tables = []

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        self._resolution = value

    @property
    def global_color_table_size(self):
        return self._global_color_table_size

    @global_color_table_size.setter
    def global_color_table_size(self, value):
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
    def comments_ex(self):
        return self._comments_extensions

    @comments_ex.setter
    def comments_ex(self, value):
        self._comments_extensions = value

    @property
    def applications_ex(self):
        return self._applications_extensions

    @applications_ex.setter
    def applications_ex(self, value):
        self._applications_extensions = value

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
        self._application_name = None
        self._identify = None
        self._data = None

    @property
    def application_name(self):
        return self._application_name

    @application_name.setter
    def application_name(self, name):
        self._application_name = name

    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, id):
        self._identify = id

    @property
    def information(self):
        return self._data

    @information.setter
    def information(self, info):
        self._data = info


class GraphicControlExtension:
    def __init__(self):
        self._disposal = None
        self._user_input_flag = None
        self._transparent_flag = None
        self._delay_time = None
        self._GCT_size = None

    @property
    def disposal(self):
        return self._disposal

    @disposal.setter
    def disposal(self, value):
        self._disposal = value

    @property
    def user_input_flag(self):
        return self._user_input_flag

    @user_input_flag.setter
    def user_input_flag(self, value):
        self._user_input_flag = value

    @property
    def transparent_flag(self):
        return self._transparent_flag

    @transparent_flag.setter
    def transparent_flag(self, value):
        self._transparent_flag = value

    @property
    def delay_time(self):
        return self._delay_time

    @delay_time.setter
    def delay_time(self, value):
        self._delay_time = value

    @property
    def GCT_size(self):
        return self._GCT_size

    @GCT_size.setter
    def GCT_size(self, value):
        self._GCT_size = value


class PlainTextExtension:
    def __init__(self):
        self._top = None
        self._left = None
        self._width = None
        self._height = None
        self._char_width = None
        self._char_height = None
        self._background_color = None
        self._text_color = None
        self._text_data = None

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def char_width(self):
        return self._char_width

    @char_width.setter
    def char_width(self, value):
        self._char_width = value

    @property
    def char_height(self):
        return self._char_height

    @char_height.setter
    def char_height(self, value):
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
    def text_data(self):
        return self._text_data

    @text_data.setter
    def text_data(self, value):
        self._text_data = value


class Image:
    def __init__(self):
        self._top = None
        self._left = None
        self._width = None
        self._height = None
        self._interlace_flag = None
        self._graphic_control_extension_index = None
        self._image_data = []
        self._local_color_table_index = None
        self._plain_text_extension_index = None

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def interlace_flag(self):
        return self._interlace_flag

    @interlace_flag.setter
    def interlace_flag(self, value):
        self._interlace_flag = value

    @property
    def graphic_control_extension_index(self):
        return self._graphic_control_extension_index

    @graphic_control_extension_index.setter
    def graphic_control_extension_index(self, value):
        self._graphic_control_extension_index = value

    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, value):
        self._image_data = value

    @property
    def local_color_table_index(self):
        return self._local_color_table_index

    @local_color_table_index.setter
    def local_color_table_index(self, value):
        self._local_color_table_index = value

    @property
    def plain_text_extension_index(self):
        return self._plain_text_extension_index

    @plain_text_extension_index.setter
    def plain_text_extension_index(self, value):
        self._plain_text_extension_index = value
