from parser import read_gif, write_gif
from gif import Gif


def main(filename: str, *, show_image: bool = False, max_clean: bool = False):
    with open(filename, "rb") as gif_file:
        gif: Gif = read_gif(gif_file, True)
        print("decoded")

    if show_image:
        print("showing images (first 5)")
        for image in gif.images[:5]:
            image.img.show()

    res = write_gif(gif, max_clean)
    with open("result.gif", "wb") as f:
        res.to_file(f)
    print("saved")


if __name__ == '__main__':
    main("gif_tests/simple/gifi.gif", show_image=False, max_clean=False)
