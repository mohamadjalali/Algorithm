from algorithms.top_one import top


a = [1, 2, 2, 3, 3, 5, 6, 3, 7, 7, 2, 9]
b = [5, 4, 7, 7, 7, 9, 9, 1, 2, 2, 2, 7, 1, 1, 1]
c = [1, 1, 2, 3, 3, 5, 5, 3, 7, 7, 2, 9]
d = [1, 1, 2, 2, 3, 4]

def test_top():
    assert top(a) == ([2, 3], 3)
    assert top(b) == ([7, 1], 4)
    assert top(c) == ([3], 3)
    assert top(d) == ([1, 2], 2)
