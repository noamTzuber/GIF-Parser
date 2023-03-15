import classes


def read_gif(filename: str):
    pass


def get_bits(byte, start, end=None):
    pass


def read_header(file, gif):
    gif.version = file.read(6)


def read_LSD(file, gif):
    block = file.read(7)
    LSD = {}
    packed = {}
    gif.width = block[0:1]
    gif.height = block[2:3]
    packedBytes = block[4]
    gif.GCT
    packed['GCTFlag'] = get_bits(packedBytes, 0)
    packed['colorResolution'] = get_bits(packedBytes, 1, 3)
    packed['sortFlag'] = get_bits(packedBytes, 4)
    packed['sizeOfGCT'] = get_bits(packedBytes, 5, 7)
    LSD['packed'] = packed
    LSD['backgroundColor'] = block[5]
    LSD['pixelAspectRatio'] = block[6]
    gif["LSD"] = LSD


def read_GCT(file, gif):
    pass


def read_Application_Extension(file, gif):
    pass


def read_Graphic_Control_Extension(file, gif):
    pass


def image_descriptor(file, gif):
    pass


def read_local_color_table(file, gif):
    pass


def read_image_data(file, gif):
    pass


def read_comment_extension(file, gif):
    pass


def read_plain_text(file, gif):
    pass