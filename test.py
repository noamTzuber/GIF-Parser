import pickle
from pathlib import Path
from typing import Literal

from decoder import decode_gif
from gif_objects import Gif


def check_file(path: Path, *, show_image: bool = False):
    with open(path, "rb") as gif_file:
        current: Gif = decode_gif(gif_file)

    with open(path.with_suffix('.pickle'), 'rb') as pickle_file:
        saved: Gif = pickle.load(pickle_file)

    print(f"file {path.stem} correctness: {current == saved}")
    if show_image:
        for img in current.images:
            img.img.show()


def save_file(path: Path):
    try:
        with open(path, "rb") as gif_file:
            gif: Gif = decode_gif(gif_file)

        with open(path.with_suffix('.pickle'), 'wb') as pickle_file:
            pickle.dump(gif, pickle_file)

        print(f"{path.stem} was saved")
    except Exception as e:
        print(f"couldn't save {path.stem}")
        print(e)


def test_gifs(*, mode: Literal['save', 'check'], files: list[str] = None, show_image: bool = False):
    if files or files == []:
        path_list = [Path(f"gif_tests/{str}.gif") for str in files]
    else:
        path_list = Path("gif_tests/").rglob('*.gif')

    for path in path_list:
        if mode == 'check':
            if path.with_suffix('.pickle').exists():
                check_file(path, show_image=show_image)
            else:
                print(f"file {path.stem} has no pickle")
        elif mode == 'save':
            save_file(path)


if __name__ == '__main__':
    test_gifs(mode='check', files=['test4'], show_image=False)
