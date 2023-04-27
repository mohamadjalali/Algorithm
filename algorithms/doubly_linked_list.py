class NodeList:
    
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
   
    # In initialization, both head and tail instance variables point to new_node.
    # And then length becomes equal to 1 due to the creation of the first node.
    def __init__(self, value):
        new_node  = NodeList(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    
    def print_list(self):
        # For navigation, the temp variable points to temp.next (next node). 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    def append(self, value):
        new_node = NodeList(value)
        # If no node exists, head and tail point to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            # For two-way communication between nodes, first the tail.next
            # node must point to the new_node node, and then new_node points
            # to the tail for the return communication.
            self.tail.next = new_node
            new_node.prev = self.tail
            # Due to reaching the last node, tail is equal to new_node.
            self.tail = new_node 
        self.length += 1
        return True


    def pop(self):
        # The temp variable is equal to the previous tail node.
        temp = self.tail.prev
        # In order to pop the last node, we have to remove the
        # references related to it, we set the tail.prev reference to None.
        self.tail.prev = None
        # temp.next, which points to the last node, is also equal to None.
        temp.next = None
        # tail is also equal to temp.
        self.tail = temp
        self.length -= 1
        return True


if __name__ == "__main__":
    linked = DoublyLinkedList(23)
    linked.append(25)
    linked.append(26)
    linked.pop()
    linked.print_list()


