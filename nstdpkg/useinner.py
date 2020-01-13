from .samelevel import another
from .inner import util


def somefunc() -> int:
    return util.func1()


if __name__ == "__main__":
    print(util.func1())
    print(util.func4())
    print(another())
