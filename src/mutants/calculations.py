""" Calculations to mutate. """

""" These are indices from external dependencies. """
METRIC_LOC = 10 
METRIC_MTTR = 21

def calculate_metric(a: int = 1, b: int = 1) -> int:
    mod = 7
    c = (a + b) % mod
    return c

def choose_metric(a: int, b: int) -> int:
    if (a < b):
        value = METRIC_LOC
    else: 
        value = METRIC_MTTR
    return value