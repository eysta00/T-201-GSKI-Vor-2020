from Node import Node

class Error(Exception):
    pass

class Empty(Error):
    pass

class LinkedStack:
    ''' LIFO Stack implementation using a singly linked list'''
    def __init__(self):
        self.size = 0
        self.head = None # Reference to the head of the list
    
    def __len__(self):
        ''' return the size '''
        return self.size
    
    def is_empty(self):
        ''' Check if list is empty'''
        return self.size == 0
    
    def push(self, value):
        ''' Add a value '''
        self.head = Node(value, self.head)
        self.size += 1

    def pop(self):
        ''' Remove and return the top element '''
        if self.is_empty():
            raise Empty('Stack is empty')
        ret_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        return ret_element

    def top(self):
        ''' Return the top element, does not remove '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element
    
    def __str__(self):
        if self.is_empty():
            raise Empty('stack is empty')
        
        ret_str = 'The Stack (Top - Bottom): '
        walk = self.head
        while walk != None:
            ret_str += str(walk.element + ' ')
            walk = walk.next
        return ret_str
    


if __name__ == "__main__":

    print("--- Test Cases ---")
    Linked_Stack = LinkedStack()
    Linked_Stack.push('a')
    Linked_Stack.push('b')
    Linked_Stack.push('c')
    Linked_Stack.push('d')
    Linked_Stack.push('e')

    print(Linked_Stack)

    print(Linked_Stack.pop())

    print(len(Linked_Stack))

    print(Linked_Stack)

    print(Linked_Stack.top())

    Linked_Stack.pop()
    Linked_Stack.pop()
    print(Linked_Stack)