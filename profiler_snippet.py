import cProfile
import pstats
import io


def profile(fun):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fun(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner


@profile
def foo():
    pass


if __name__ == '__main__':
    foo()
