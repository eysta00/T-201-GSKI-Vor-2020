class LinkedStack:

    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        
        __slots__ = '_element', '_next' # streamline memory usage

        def __init__ (self, element, next): # initialize node’s fields
            self.element = element # reference to user’s element
            self.next = next # reference to next node

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        '''Return true if stack is empty'''
        return self.size == 0

    def push(self, e):
        self.head = _Node(e, self.head)
        self.size += 1
    
    def top(self):
        '''Return (but do not remove) the element at the top of the stack. 
        Raise Empty exception if the stack is empty.'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element #Top of stack of list

    def pop(self):
        ''' Remove and return the element from the top of the stack (i.e., LIFO). 
        Raise Empty exception if the stack is empty. '''
        if self.empty():
            raise Empty('Stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer
    

def printList(head):
    if head == None:
        print()
    print(head.data, end=" ")
    printList(head.next)


Singly_list = LinkedStack()
Singly_list.push(1)
Singly_list.push(2)
Singly_list.push(3)
Singly_list.push(4)
printList(Singly_list)