from algorithms.doubly_linked_list import DoublyLinkedList



def test_doubly_linked_list():
    # Create new doubly linked list.
    dll = DoublyLinkedList(10)

    # Test the append method.
    assert dll.append(20) == True
    assert dll.append(30) == True
    assert dll.length == 3
    
    # Test the pop method.
    assert dll.pop().value == 30
    assert dll.length == 2

    # Test the print_list method
    dll.print_list()
    assert True

    # Test the prepend method.
    assert dll.prepend(0) == True
    assert dll.length == 3

    # Test the insert method.
    # assert dll.insert(1, 5)
