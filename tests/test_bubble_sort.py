from algorithms.bubble_sort import bubble_sort



def test_bubble_sort():
    assert bubble_sort([4, 2, 6, 5, 1, 3])  == [1, 2, 3, 4, 5, 6]
    assert bubble_sort([10, 50, 20, 0, 40]) == [0, 10, 20, 40, 50]
    assert bubble_sort([-1, -5, 0, 9, 5, 1])  == [-5, -1, 0, 1, 5, 9]

