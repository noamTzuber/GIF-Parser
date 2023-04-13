import pickle

from decoder import decode_gif
from gif_objects import Gif


def main(save: bool):
    with open("gif_tests/test1.gif", "rb") as gif_file:
        gif: Gif = decode_gif(gif_file)
        current = pickle.dumps(gif)

    if save:
        with open('gif_tests/test1.pickle', 'wb') as handle:
            pickle.dump(gif, handle)
        print("saved")

    else:
        with open('gif_tests/test1.pickle', 'rb') as f:
            data = f.read()
            print(f"are the same: {data == current}")


if __name__ == '__main__':
    main(False)
