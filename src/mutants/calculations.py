""" Calculations to mutate. """


def calculate_metric(a: int = 1, b: int = 1) -> int:
    mod = 3
    c = (a + b) % mod
    return c


def choose_metric(a: int = 1, b: int = 1) -> int:
    if a < b:
        value = 10
    else:
        value = 21
    return value
