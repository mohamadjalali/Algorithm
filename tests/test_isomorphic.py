from algorithms.isomorphic import is_isomorphic



def test_isomorphic():
    # Must be return False
    assert is_isomorphic('bar', 'foo') == False
    # Must be return True
    assert is_isomorphic('abc', 'bcd') == True
    # Due to the unequal number of characters in the
    # received arguments, the condition becomes False.
    assert is_isomorphic('tar', 'rafe') == False
