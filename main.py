from pprint import pprint

from decoder import decode_gif
from gif_objects import Gif


def main():
    with open("gif_tests/giphy.gif", "rb") as gif_file:
        gif: Gif = decode_gif(gif_file)
    pprint(gif)


if __name__ == '__main__':
    main()
