class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    
    def __init__(self):
        self.root = None


    def insert(self, value):
        # create a new node with the given value        
        new_node = Node(value)
        # if the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return True
        
        # set a temporary node to the root of the tree
        temp = self.root
        while (True):
            # if the value already exists in the tree, return False
            if new_node.value == temp.value:
                return False
            
            # if the value is less than the temporary node's value, go left.
            if new_node.value < temp.value:
                # if there's no left child, insert the new node as the left child.
                if temp.left is None:
                    temp.left = new_node
                    return True
                # otherwise, continue iterating through the left subtree
                temp = temp.left
            
            # if the value is greater than the temporary node's value, go right
            else:
                # if there's no right child, insert the new node as the right child
                if temp.right is None:
                    temp.right = new_node
                    return True
                # otherwise, continue iterating through the right subtree
                temp = temp.right


    def contains(self, value):
        # start at the root of the tree
        temp = self.root
        # iterate through the tree until the node
        # is found or the end of the tree is reached.
        while temp is not None:
            # if the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left
            
            # if the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            
            # if the value maches the current node's value, return True
            else:
                return True
        # if the value is not found in the tree, return False
        return False



if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)


    print(my_tree.contains(52))
    print(my_tree.contains(18))
    print(my_tree.contains(15))

