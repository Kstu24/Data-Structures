"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# import sys
# print(sys.path)
from queue import Queue

class Node: 
     def __init__(self,value):
         self.value = value
         self.next = None

     def get_value(self):
         return self.value

     def get_next(self):
         return self.next

     def set_next(self, new_text): 
         self.next = new_text

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the last node's "next_node" to the new node
            self.tail.set_next(new_node) # (last node in chain).next_node = new_node
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    def remove_tail(self):
        """
        remove the last node in the chain and return its value
        """
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if there is only one node
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # remove the node
            # set head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        # otherwise
        else:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # we need to set the "self.tail" to the second to last node
            # we can only do this by traversing the whole list from beginning to end

            # starting from the head
            current_node = self.head

            # keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                # keep looping
                current_node = current_node.get_next()

            # at the end of the iteration set "self.tail" to the current_node
            self.tail = current_node
            # set the new tail's "next_node" to None
            self.tail.set_next(None)
            # return Value
            return value

    def remove_head(self):
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            # set head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        else:
            # store the old head's value
            value = self.head.get_value()
            # set self.head to old head's next
            self.head = self.head.get_next()
            # return the value
            return value 

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            tail_removed = self.storage.remove_tail()
            self.size -= 1
            return tail_removed

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue
        bft = Queue()
        # enqueue the first node (self)
        bft.put(node)

        # while there is data on the queue
        while not bft.empty():
            # dequeu from queue on to current_node
            node = bft.get()
            # print the current_node's value
            print(node.value)
            # if the current_node has a left child
            if node.left:
                # enqueue the left child
                bft.put(node.left)
            # if the current_node has a right child
            if node.right:
                # enqueue the right child
                bft.put(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)
        # pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
        # pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
bst.pre_order_dft(bst)
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft(bst)  
