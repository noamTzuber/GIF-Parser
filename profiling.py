import cProfile
import pstats
import subprocess

import lzw
import main
import timeit

from utils import chunker


def profile(function, *args, **kwargs):
    with cProfile.Profile() as pr:
        function(*args, **kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='profiling.prof')
    subprocess.run(['snakeviz', 'profiling.prof'])


def time_it(function, n: int, *args, **kwargs):
    t = timeit.Timer(lambda: function(*args, **kwargs))
    time = t.timeit(n)
    print(f"{function.__name__}, {n} runs, total: {time}, average: {time / n}")


def flip_data(compress_data):
    fliped_data = ''
    length = len(compress_data) / 8
    for i in range(int(length)):
        fliped_data += compress_data[-8:]
        compress_data = compress_data[:-8]

    bytes_object = fliped_data.encode("utf-8")

    return bytes_object


def flip_data2(compress_data):
    flipped_data = ''
    chunked = [x for x in chunker(8, compress_data)]
    for chunk in reversed(chunked):
        flipped_data += chunk

    bytes_object = flipped_data.encode("utf-8")

    return bytes_object


def flip_data3(compress_data):
    chunked = [x for x in chunker(8, compress_data)]
    fliped_data = ''.join(reversed(chunked))

    bytes_object = fliped_data.encode("utf-8")

    return bytes_object


def flip_data4(compress_data):
    fliped_data = ''.join(compress_data[i:i + 8][::-1] for i in range(0, len(compress_data), 8))
    bytes_object = fliped_data.encode("utf-8")
    return bytes_object


if __name__ == '__main__':
    # profile(main.main, "gif_tests/test4.gif", show_image=True)
    s = "08010020080100200801002008010020080100200801002008010020" * 1000
    n = 1000
    time_it(flip_data, n, s)
    time_it(flip_data2, n, s)
    time_it(flip_data3, n, s)
    time_it(flip_data4, n, s)
