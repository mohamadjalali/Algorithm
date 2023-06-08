from algorithms.merge import merge


def test_merge():
    assert merge([1, 3, 4], [2, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([0, 3, 5, 7], [1, 2, 4, 8]) == [0, 1, 2, 3, 4, 5, 7, 8]

