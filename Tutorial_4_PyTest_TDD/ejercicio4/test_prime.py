import pytest

# Test values from 0 to 19
TEST_VALUES = [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

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

@pytest.mark.parametrize('num', [i for i in range(20)])
def test_prime(num):
    assert is_prime(num) == TEST_VALUES[num]