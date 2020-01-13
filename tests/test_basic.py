from nstdpkg import samelevel
from nstdpkg.inner import util

def test_samelevel():
    data = samelevel.another()
    assert data == "just some data"

def test_util():
    print(util.func1())
    print(util.func2())
    print(util.func3())
    print(util.func4())
