import cProfile
import pstats
import main


def profile(function, *args, **kwargs):
    with cProfile.Profile() as pr:
        function(*args, **kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='profiling.prof')


if __name__ == '__main__':
    profile(main.main, "gif_tests/test4.gif", show=True)
