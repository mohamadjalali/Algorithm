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
        # Returns None if there are no nodes.
        if self.length == 0:
            return None

        # The tail variable represents the popped node,
        # which is finally returned as the popped node.
        temp = self.tail
        # If there is a node, head and tail are equal to None,
        if self.length ==1:
            self.head = None
            self.tail = None

        else:
            # The tail becomes equal to its previous node.
            self.tail = self.tail.prev
            # The tail.next node points to None.
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    
    def prepend(self, value):
        new_node = NodeList(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # To link (next) the new node with head
            new_node.next  = self.head
            # Also, to connect the return link (prev) with the new node, we act as follows.
            self.head.prev = new_node
            # As a rule, the new_node node, which represents the first node, its arrow(prev) should point to None.
            new_node.prev = None
            # Finally, the head node must point to new_node.
            self.head = new_node
        self.length += 1
        return True



if __name__ == "__main__":
    linked = DoublyLinkedList(23)
    linked.append(25) 
    linked.prepend(1)
    linked.print_list()


