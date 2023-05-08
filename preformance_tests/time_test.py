import cProfile
import pstats
import subprocess

import lzw
import main
import timeit
from types import FunctionType
from typing import Callable, List

from attrs import define

from utils import chunker


@define
class Result:
    name: str
    runs: int
    total_time: float

    @property
    def average(self):
        return self.total_time / self.runs

    def __repr__(self):
        return f"{self.name}, {self.runs} runs, total: {self.total_time}, average: {self.average}"


def time_it(n_runs: int, function: callable, *args, **kwargs) -> Result:
    t = timeit.Timer(lambda: function(*args, **kwargs))
    time = t.timeit(n_runs)
    return Result(function.__name__, n_runs, time)


def test_functions(n_runs: int, functions: List[callable], *args, **kwargs):
    """
    the first function is treated as the truth, and every other function is
    """
    if not functions:
        return

    output = functions[0](*args, **kwargs)


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
