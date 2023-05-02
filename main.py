import pstats
from pprint import pprint

import pickle

import post_prossesing
from decoder import decode_gif
from gif_objects import Gif


def main(filename: str, *, show_image: bool = False, from_pickle: bool = False):
    with open(filename, "rb") as gif_file:
        gif: Gif = decode_gif(gif_file)

    pprint(gif)
    if show_image:
        for image in gif.images:
            image.img.show()

    post_prossesing.color_table_processes(gif)


if __name__ == '__main__':
    main("gif_tests/test4.gif", show_image=False)
