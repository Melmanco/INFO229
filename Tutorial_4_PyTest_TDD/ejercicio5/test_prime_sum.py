import pytest

# Generates lists of numbers
TEST_LISTS=[
    [i for i in range(10)], # sum = 17
    [i for i in range(10,20)], # sum = 60
    [i for i in range(20)], # sum = 77
    [i for i in range(20,30)], # sum = 52
    [i for i in range(30)], # sum = 129
]

# List of sums corresponding to each list
TEST_VALUES=[17,60,77,52,129]

def is_prime(num):

    # Prime numbers must be greater than 1
    if num < 2:
        return False
    
    if num == 2:
        return True

    # If it's even
    if num % 2 == 0:
        return False

    if num == 3:
        return True

    # Check all odd numbers from 3 to num/2,
    # since num/2 is the higher number that
    # could divide num
    for n in range(3, num//2, 2):
        if num % n == 0:
            return False

    return True

def sum_of_primes(values):
    sum = 0
    for value in values:
        if is_prime(value):
            sum += value

    return sum

@pytest.mark.parametrize('n', [i for i in range(5)])
def test_prime(n):
    assert sum_of_primes(TEST_LISTS[n]) == TEST_VALUES[n]