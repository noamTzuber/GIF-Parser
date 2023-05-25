from pprint import pprint

from decoder import *
from writer import write_gif


def main(filename: str, *, show_image: bool = False):
    with open(filename, "rb") as gif_file:
        gif: Gif = decode_gif(gif_file)
        print("decoded")

    pprint(gif)
    if show_image:
        for image in gif.images:
            image.img.show()

    with open("result.gif", "wb") as f:
        res = write_gif(gif)
        res._stream.tofile(f)
        print("saved")


if __name__ == '__main__':
    main("gif_tests/giphy.gif", show_image=True)
