import pytest

# Generates test words
TEST_VALUES = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".split(' ')

# Inverse text
def inverse(s):
    new_string = ''

    for char in s:
        new_string = char + new_string

    return new_string

# Tests inverse() with python's 'actual way' of reversing strings
@pytest.mark.parametrize('word', TEST_VALUES)
def test_inverse(word):
    assert inverse(word) == word[::-1]
