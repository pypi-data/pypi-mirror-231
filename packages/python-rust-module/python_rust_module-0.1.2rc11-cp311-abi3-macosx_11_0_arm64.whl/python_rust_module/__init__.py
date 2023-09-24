from .python_rust_module import sum_as_string, sum_to_n


def rust_sum_to_n(n):
    return sum_to_n(n)


def python_sum_to_n(n):
    return sum(range(1, n + 1))
