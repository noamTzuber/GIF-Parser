from decoder import decode_gif
from gif_objects import Gif
from writer import write_gif


def main(filename: str, *, show_image: bool = False):
    with open(filename, "rb") as gif_file:
        gif: Gif = decode_gif(gif_file)
        print("decoded")

    if show_image:
        print("showing images (first 5)")
        for image in gif.images[:5]:
            image.img.show()

    with open("result.gif", "wb") as f:
        res = write_gif(gif)
        res.to_file(f)
        print("saved")


if __name__ == '__main__':
    # i = ["simple/gifi.gif","simple/gifi1.gif","simple/gifi2.gif","simple/gifi3.gif"]
    # for gi in i :
    main("gif_tests/simple/gifi.gif", show_image=False)
