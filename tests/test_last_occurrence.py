from algorithms.last_occurrence import last_occurrence as lo

a = [2, 2, 3, 4, 5, 5, 6, 6, 7, 7]

def test_last_occurrence():

    assert lo(a, 2) == 1
    assert lo(a, 3) == 2
    assert lo(a, 4) == 3
    assert lo(a, 5) == 5
    assert lo(a, 7) == 9

