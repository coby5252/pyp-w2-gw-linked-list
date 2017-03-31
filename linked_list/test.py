from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is not None and len(elements) > 0:
            self.start = Node(elements.pop(len(elements) - 1))
            self.end = self.start
            while len(elements) > 0:
                self.start = Node(elements.pop(len(elements) - 1), next = self.start)
        else:
            pass

    def __str__(self):
        pass
        
    def __len__(self):
        ret = 0
        x = self.start
        while x is not None:
            ret += 1
            x = x.next
        return ret


x = LinkedList([1,2,3,4])

print(len(x))