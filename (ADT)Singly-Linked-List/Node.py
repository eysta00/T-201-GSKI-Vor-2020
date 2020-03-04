class Node:
    '''A node for a singly linked list
    (element = None, next = None)
    '''
    __slots__ = 'element', 'next'

    def __init__(self, element = None, next = None):
        self.element = element
        self.next = next