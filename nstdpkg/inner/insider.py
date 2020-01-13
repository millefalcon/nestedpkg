def func() -> int:
    return 45


def awesome_func(vals) -> str:
    return "*".join(str(x) for x in vals)  # make it work: for things like `int`s
