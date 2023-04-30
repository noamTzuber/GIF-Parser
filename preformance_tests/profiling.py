import cProfile
import os
import pstats
import subprocess
from typing import Callable, Literal

import main


def profile(function: Callable, tool: Literal['snakeviz', 'tuna'], *args, **kwargs):
    with cProfile.Profile() as pr:
        function(*args, **kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='../profiling.prof')
    subprocess.run([tool, 'profiling.prof'])

if __name__ == '__main__':
    profile(main.main, 'snakeviz', "gif_tests/test4.gif", show_image=False)