import math

from bitstring import ConstBitStream

import classes
from lzw import decode


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
    # before getting in we create image and add it to the gif anf the gif will send to this function
    # and add the last gce to this image

    current_image = gif.images[-1]

    current_image.left = int.from_bytes(file.read(2), "big")
    current_image.top = int.from_bytes(file.read(2), "big")
    current_image.width = int.from_bytes(file.read(2), "big")
    current_image.height = int.from_bytes(file.read(2), "big")

    stream = ConstBitStream(file.read(1))

    current_image.local_color_table_flag = stream.read('bin1')
    current_image.interlace_flag = stream.read('bin1')

    # those attributes are not necessary for the gif
    # sort_flag = stream.read('bin1')
    # reserved_for_future_use = stream.read('bin2')
    # size_of_local_color_table = stream.read('bin3')


def read_local_color_table(file, gif):
    pass


def read_image_data(file, gif):
    bytes_image_data = b''
    # current_image = gif.images[-1]

    lzw_minimum_code_size = int.from_bytes(file.read(1),"big")
    index_length = math.ceil(math.log(lzw_minimum_code_size + 1)) + 1

    while (number_of_sub_block_bytes := file.read(1)) != b'\x00':
        compressed_sub_block = (file.read(int.from_bytes(number_of_sub_block_bytes, "big"))).hex()
        bytes_image_data += decode(compressed_sub_block, math.pow(2, lzw_minimum_code_size))

    # local_color_table = gif.LCTs[-1]

    # pos = 0
    # for i in range(int(len(bytes_image_data)/index_length)):
    #     current_image.image_data.append(local_color_table[bytes_image_data[pos:pos+index_length]])
    #     pos += index_length


def read_comment_extension(file, gif):
    pass


def read_plain_text(file, gif):
    pass