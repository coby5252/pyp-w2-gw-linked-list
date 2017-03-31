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
            self.start = None
            self.end = self.start

    def __str__(self):
        ret = []
        for node in self:
            ret.append(node.elem)
        return str(ret)
    
    def __len__(self):
        ret = 0
        for node in self:
            ret += 1
        return ret
        

    def __iter__(self):
        x = self.start
        while x is not None:
            yield x
            x = x.next
        raise StopIteration()
            

    def __getitem__(self, index):
        counter = 0
        for node in self:
            if(counter == index):
                return node.elem
            counter += 1
        raise IndexError()
        

    def __add__(self, other):
        if self.start is None and other.start is None:
            return self
        elif self.start is None:
            return other
        elif other.start is None:
            return self
            
        ret = LinkedList()
        for node in self:
            ret.append(node.elem)
        for node in other:
            ret.append(node.elem)
        return ret
    

    def __iadd__(self, other):
        self = self + other
        return self

    def __eq__(self, other):
        if self.start is None and other.start is None:
            return True
        elif self.start is None:
            return False
        elif other.start is None:
            return False
            
        a_node = self.start
        b_node = other.start
        
        while a_node.next is not None:
            if a_node.elem != b_node.elem:
                return False
            a_node = a_node.next
            if b_node.next is None:
                return False
            b_node = b_node.next
        
        return b_node.next is None
    
    def __ne__(self, other):
        return not self.__eq__(other)
        
        
    def append(self, elem):
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
            self.end = self.start
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        return len(self)



    def pop(self, index=None):
        last_element = self.start
        if self.start == None:
            raise IndexError()
        if index is None:
            index = len(self) - 1
                
        if len(self)-1 < index:
            raise IndexError()
        
        if index == 0:
            ret = self.start.elem
            self.start = self.start.next
            return ret
            
        for counter, node in enumerate(self):
            if counter == index:
                last_element.next = node.next
                
                if node == self.end:
                    self.end = last_element
            
                
                return node
            last_element = node