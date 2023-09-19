import argparse
from fib_py.fib_calcs.fib_number import iter_fib_number


def fib_numb() -> None:
    parser = argparse.ArgumentParser(description="Calculate fibonacci numbers")
    parser.add_argument(
        "--number",
        action="store",
        type=int,
        required=True,
        help="Fibonacci number to be calculated",
    )

    args = parser.parse_args()
    res_fib_num = iter_fib_number(args.number)
    print(f"Your fibonacci number is : {res_fib_num}")
