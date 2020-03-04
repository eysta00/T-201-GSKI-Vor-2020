from Node import Node

class Error(Exception):
    pass

class Empty(Error):
    pass

class LinkedQueue:
    ''' FIFO Stack implementation using a singly linked list'''
    def __init__(self):
        self.size = 0
        self.head = None # Reference to the head of the list
        self.tail = None # Reference to the tail of the list

    def __len__(self):
        ''' return the size '''
        return self.size
    
    def is_empty(self):
        ''' Check if list is empty'''
        return self.size == 0
    
    def enqueu(self, value):
        ''' Add a value to back the of queue '''
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        ''' Remove and return the last element '''
        if self.is_empty():
            raise Empty('Stack is empty')
        ret_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None # Special case if head is last element
        return ret_element

    def first(self):
        ''' Return the first element, does not remove '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element
    
    def __str__(self):
        if self.is_empty():
            raise Empty('stack is empty')
        
        ret_str = 'The Stack (Front - Back): '
        walk = self.head
        while walk != None:
            ret_str += str(walk.element + ' ')
            walk = walk.next
        return ret_str
    


if __name__ == "__main__":

    print("--- Test Cases ---")
    Linked_Queue = LinkedQueue()
    Linked_Queue.enqueu('a')
    Linked_Queue.enqueu('b')
    Linked_Queue.enqueu('c')
    Linked_Queue.enqueu('d')
    Linked_Queue.enqueu('e')

    print(Linked_Queue)

    print(Linked_Queue.dequeue())

    print(len(Linked_Queue))

    print(Linked_Queue)

    print(Linked_Queue.first())

    Linked_Queue.dequeue()
    Linked_Queue.dequeue()
    print(Linked_Queue)