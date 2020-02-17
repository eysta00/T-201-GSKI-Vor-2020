class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    # Time complexity O(1) apart from __str__
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def push_back(self, val):
        '''Add a value to back(tail) of list '''
        new_tail = Node(val)
        if self.is_empty(): # The only node is head and tail
            self.tail , self.head = new_tail, new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

        self.size += 1

    def push_front(self, val):
        '''Add a value to front(head) of list '''
        new_head = Node(val, self.head)
        self.head = new_head
        if self.is_empty():
            self.tail = self.head

        self.size += 1

    def pop_front(self):
        '''Remove and return the first item'''
        if not self.is_empty():
            val = self.head.data
            self.head = self.head.next
            self.size -= 1

            return val

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        '''Return a string of all items '''
        ret_str = ""
        node = self.head
        
        try:
            while node.next != None:
                ret_str += str(node.data) + " "
                node = node.next
            return ret_str + str(node.data)
        except:
            return ret_str
            

