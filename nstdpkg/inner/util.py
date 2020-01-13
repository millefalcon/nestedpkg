# relative imports
# from inner import insider # this works, but is a bit weird
from . import insider  # consider using this
from ..samelevel import another

from nstdpkg.inner.insider import awesome_func


def func1() -> int:
    return 42


def func2() -> int:
    data = insider.func()
    return data


def func3() -> str:
    return another()


def func4() -> str:
    return awesome_func(range(10))
