class NodeList:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None


class DoublyLinkedList:
    
    def __init__(self, value):
        new_node = NodeList(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = NodeList(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node 
        self.length += 1
        return True

    def pop(self):
        temp = self.tail.prev
        self.tail.prev = None
        temp.next = None
        self.tail = temp
        self.length -= 1
        return True


if __name__ == "__main__":
    linked = DoublyLinkedList(23)
    linked.append(25)
    linked.append(26)
    linked.pop()
    linked.print_list()

