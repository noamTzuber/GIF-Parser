import pickle
from pathlib import Path

from decoder import decode_gif
from gif_objects import Gif
from writer import write_gif


def load_gif_from_pickle(path: Path) -> Gif:
    with open(path.with_suffix('.pickle'), 'rb') as pickle_file:
        gif = pickle.load(pickle_file)
    print("loaded from pickle")
    return gif


def save_gif_to_pickle(path: Path, gif: Gif) -> None:
    with open(path.with_suffix('.pickle'), 'wb') as pickle_file:
        pickle.dump(gif, pickle_file)
    print("saved new pickle")


def read_gif(path: Path) -> Gif:
    with open(path.with_suffix(".gif"), "rb") as gif_file:
        gif = decode_gif(gif_file)
    print("decoded gif")
    return gif


def write_gif2(path: Path, gif: Gif) -> None:
    with open(path.with_stem(f"{path.stem}-result").with_suffix(".gif"), "wb") as gif_file:
        res = write_gif(gif)
        res.to_file(gif_file)
    print("wrote gif")


def main(filename: str, *, show_image: bool = False):
    path = Path(filename)

    if path.with_suffix(".pickle").exists():
        choice = input("would you like to open saved pickle file? [y/n]: ")
        if choice == "y":
            gif = load_gif_from_pickle(path)
        elif choice == "n":
            gif = read_gif(path)
            save_gif_to_pickle(path, gif)
        else:
            print("write y or n in lower case, bro")
            return
    else:
        gif = read_gif(path)
        save_gif_to_pickle(path, gif)

    if show_image:
        print("showing images (first 5)")
        for image in gif.images[:5]:
            image.img.show()

    write_gif2(path, gif)


if __name__ == '__main__':
    main("gif_tests/test11.gif", show_image=False)
