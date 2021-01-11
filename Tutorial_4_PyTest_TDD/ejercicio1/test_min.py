import random
import pytest

# Generate list of 10 lists with numbers from 1 to 10 in random order,
# to make sure it is actually getting the min value
def get_test_values():
    l = [[i for i in range(10)] for i in range(10)]
    for values_list in l:
        random.shuffle(values_list)

    return l

TEST_VALUES = get_test_values()

# Gets min value from list
def get_min(values):
    min = values[0]
    for value in values:
        if value < min:
            min = value

    return min

# Test get_min() with random lists
@pytest.mark.parametrize("values", TEST_VALUES)
def test_min(values):
    assert get_min(values) == min(values)