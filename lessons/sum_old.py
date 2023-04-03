"""Example function for Unit Tests"""

def sum(xs: list[float]) -> float:
    """returm sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
    return sum_total