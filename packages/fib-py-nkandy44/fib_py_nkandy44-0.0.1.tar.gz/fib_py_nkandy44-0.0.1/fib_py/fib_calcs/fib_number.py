from typing import Optional


def iter_fib_number(n: int) -> Optional[int]:
    if n < 0:
        raise ValueError("Fibonacci has to be equal or above zero")
    elif n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(0, n - 1):
            c = a + b
            a, b = b, c
        return b
