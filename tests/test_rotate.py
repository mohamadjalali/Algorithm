from algorithms.rotate import rotate




def test_rotate():
    assert rotate("Hello", 2) == 'lloHe'
    assert rotate("World", 3) == 'ldWor'
    assert rotate("Scotland", 5) == 'andScotl'

