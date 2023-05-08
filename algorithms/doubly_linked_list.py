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
    

#    def pretty_print_list(self):
#        # For navigation, the temp variable points to temp.next (next node). 
#        temp = self.head
#        print("None", end="")
#        while temp is not None:
#            print(f" <- {temp.value} -> ", end='')
#            temp = temp.next
#        print("None")
 
   
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
            # As a rule, the new_node node, which represents the first
            # node, its arrow(prev) should point to None.
            new_node.prev = None
            # Finally, the head node must point to new_node.
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        temp = self.head
        # Returns None if there are no nodes.
        if self.length == 0:
            return None
        # If there is a node, head and tail are equal to None,
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            # The head node points to the next node because the current head will be popped.
            self.head = self.head.next
            # Because the first node is head, that's why the prev arrow points to None.
            self.head.prev = None
            # Finally, temp.prev points to None because
            # temp shouldn't point to any nodes.
            temp.next = None
        self.length -= 1
        return temp


    def get(self, value):
        if value < 0 or value >= self.length:
            return None
        temp = self.head
        # To improve the function, we compare the value with the total number of nodes, if
        # it is less than the total average, we start from the first node and vice versa.
        if value < self.length / 2:
            for _ in range(value):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, value, -1):
                temp = temp.prev
        return temp


    def set_value(self, index, value):
        # We use the get method to get the index node. and then if it is 
        # true (according to the return value of the get method),
        # we change the value of the mentioned node.
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        # We use prepend method to avoid to more coding.
        if index == 0:
            return self.prepend(value)

        # If the index is equal to the length,
        # use the append method.
        if index == self.length:
            return self.append(value)

        else:
            new_node = NodeList(value)
            # First, we specify the before and next nodes
            before = self.get(index - 1)
            after  = before.next
            # The prev and next pointers of the new_node
            # point to the before and after nodes.
            new_node.prev  = before
            new_node.next  = after
            # Then we do the same thing in reverse, that is, before
            # and after nodes point to our node between them, i.e. new_node.
            before.next = new_node
            after.prev  = new_node

        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        # In the following, we have two else, if one is more readable
        # than the other, then comment one of elses and uncomment the other.
        else:
            temp = self.get(index)

            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None

#        else:
#            before = self.get(index - 1)
#            after  = before.next.next
#            before.next = after
#            after.prev  = before

        self.length -= 1
        return temp

    
    # In the near future, the following method will be completed.
    def reverse(self):
        pass


    def reverse_v1(self):
        temp = None
        current = self.head
  
        # Swap next and prev for all nodes 
        # of doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
  
        # Before changing head, check for the
        # cases like empty list and list with 
        # only one node
        if temp is not None:
            self.head = temp.prev
  
    # Given a reference to the head of a list 
    # and an integer,inserts a new node on the 
    # front of list


    def reverse_v2(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev

            # move to the next node
            temp = temp.prev

        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head


if __name__ == "__main__":
    linked = DoublyLinkedList(1)
    linked.append(2) 
    linked.append(4)
    linked.reverse_v2()
    linked.print_list()

