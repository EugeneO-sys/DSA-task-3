"""Question 4 - Recursive programs."""


def sum_natural(n: int) -> int:
    """Sum of the first n natural numbers: S(n) = n + S(n-1), S(0) = 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:                      # base case
        return 0
    return n + sum_natural(n - 1)   # recursive case


def factorial(n: int) -> int:
    """n! = n * (n-1)!, 0! = 1."""
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    if n <= 1:                      # base case
        return 1
    return n * factorial(n - 1)


def fib(n: int) -> int:
    """Nth Fibonacci term with F(0)=0, F(1)=1."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:                       # base cases
        return n
    return fib(n - 1) + fib(n - 2)


def fib_series(n: int, a: int = 0, b: int = 1) -> list:
    """Generate the first n Fibonacci terms recursively (linear time:
    the two latest terms are carried as arguments)."""
    if n <= 0:
        return []
    return [a] + fib_series(n - 1, b, a + b)


if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} natural numbers : {sum_natural(n)}")
    print(f"Factorial of 5                  : {factorial(5)}")
    print(f"10th Fibonacci term (F10)       : {fib(10)}")
    print(f"First 10 Fibonacci terms        : {fib_series(10)}")
    # self-checks
    assert sum_natural(100) == 100 * 101 // 2
    assert factorial(0) == 1 and factorial(6) == 720
    assert [fib(i) for i in range(8)] == fib_series(8)
    print("All checks passed.")
