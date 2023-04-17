import pickle
from pathlib import Path
from pprint import pprint
from typing import Literal

from decoder import decode_gif
from gif_objects import Gif


def check_file(path):
    with open(path, "rb") as gif_file:
        current: Gif = decode_gif(gif_file)

    with open(path.with_suffix('.pickle'), 'rb') as pickle_file:
        saved: Gif = pickle.load(pickle_file)

    print(f"file {path.stem} correctness: {current == saved}")
    #pprint(current)
    for img in current.images:
        img.img.show()


def save_file(path):
    try:
        with open(path, "rb") as gif_file:
            current: Gif = decode_gif(gif_file)

        with open(path.with_suffix('.pickle'), 'wb') as pickle_file:
            pickle.dump(current, pickle_file)

        print(f"{path.stem} was saved")
    except Exception as e:
        print(f"couldn't save {path.stem}")
        print(e)


def main(*, save: Literal['save', 'check']):
    path_list = Path("gif_tests").rglob('*.gif')
    for path in path_list:
        if save == 'check' and path.with_suffix('.pickle').exists():
            check_file(path)

        if save == 'save':
            save_file(path)


if __name__ == '__main__':
    main(save='check')
