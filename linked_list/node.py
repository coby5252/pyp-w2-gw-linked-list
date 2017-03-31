class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        myVal = "Node(" + str(self.elem) + ")"
        nextVal = "/"
        if self.next is not None:
            nextVal = "Node(" + str(self.next.elem) + ")"
        return "%(val)s > %(next_node)s"%{'val': myVal, 'next_node': nextVal}

    def __eq__(self, other):
        return self.elem == other

    def __repr__(self):
        pass
