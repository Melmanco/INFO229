import pytest

# List of Fibonacci sequence
FIBONACCI_VALUES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]

# Generates list of values from 0 to 14
TEST_VALUES = [i for i in range(15)]

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# Tests fibonacci() with actual Fibonacci numbers
@pytest.mark.parametrize('num', TEST_VALUES)
def test_fibonacci(num):
    assert fibonacci(num) == FIBONACCI_VALUES[num]