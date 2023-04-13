from algorithms.occurrence import first_occurrence as fo



a = [2, 2, 3, 4, 5, 5, 6, 6, 7, 7]

def test_first_occurrence():

    assert fo(a, 3) == 2
    assert fo(a, 2) == 0
    assert fo(a, 6) == 6
    assert fo(a, 7) == 8
    assert fo(a, 5) == 4

