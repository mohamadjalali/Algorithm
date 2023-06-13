from algorithms.merge import merge_sort


def test_merge_sort_sort():
    assert merge_sort([1, 3, 4, 2, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sort([0, 3, 5, 7, 1, 2, 4, 8]) == [0, 1, 2, 3, 4, 5, 7, 8]

