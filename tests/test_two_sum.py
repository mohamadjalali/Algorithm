from algorithms.two_sum import two_sum


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 18) == [1, 2]
    assert two_sum([3, 5, 8, 9, 10], 13) == [0, 4]
    assert two_sum([1, 4, 6, 15, 20, 30], 23) == None
    assert two_sum([1, 4, 6, 15, 20, 30], 23) == None
    # It should be None because it is not sorted
    assert two_sum([40, 21, 31, 10, 3, 2, 1], 15) == None

