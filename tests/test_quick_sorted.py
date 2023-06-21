from algorithms.quick_sorted import quick_sort


def test_quick_sorted():
    # First we take the unordered lists.
    my_list_1 = [4, 2, 6, 5, 1, 3]
    my_list_2 = [10, 50, 20, 0, 40]
    my_list_3 = [-1, -5, 0, 9, 5, 1]
    # The following function takes the corresponding list and sorts it.
    quick_sort(my_list_1)
    quick_sort(my_list_2)
    quick_sort(my_list_3)
    # Finally, It compares the lists with the expected lists.
    assert my_list_1 == [1, 2, 3, 4, 5, 6]
    assert my_list_2 == [0, 10, 20, 40, 50]
    assert my_list_3 == [-5, -1, 0, 1, 5, 9]


