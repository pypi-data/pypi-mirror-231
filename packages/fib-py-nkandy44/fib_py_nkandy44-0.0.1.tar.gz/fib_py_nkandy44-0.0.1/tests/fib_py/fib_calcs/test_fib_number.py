from unittest import main, TestCase
from fib_py.fib_calcs.fib_number import iter_fib_number


class IterativeFibNumberTest(TestCase):
    def test_zero(self):
        self.assertEqual(0, iter_fib_number(n=0))

    def test_negative(self):
        with self.assertRaises(ValueError) as raised_error:
            iter_fib_number(n=-1)
        self.assertEqual(
            "Fibonacci has to be equal or above zero", str(raised_error.exception)
        )

    def test_one(self):
        self.assertEqual(1, iter_fib_number(n=1))

    def test_two(self):
        self.assertEqual(1, iter_fib_number(n=2))

    def test_twenty(self):
        self.assertEqual(6765, iter_fib_number(n=20))


if __name__ == "__main__":
    main()
