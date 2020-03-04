from Node import Node

class Error(Exception):
    pass

class Empty(Error):
    pass

class LinkedDeQue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


    def __len__(self): # Big O(1)
        return self.size

    def is_empty(self): # Big O(1)
        return self.size == 0


    def add_last(self, value): # Big O(1)
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
            
    
    def add_first(self, value): # Big O(1)
        new_node = Node(value, None)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1    
    
    def delete_last(self): # big O(n)
        if self.is_empty():
            raise Empty('DeQue is empty')

        walk = self.head

        self.size -= 1
        if self.is_empty(): # Special case if only one node
            ret_element = walk.element
            self.head = None
            self.tail = None
            return ret_element


        while walk.next.next != None: # Gotta check ahead of two nodes
            walk = walk.next

        ret_element = walk.next.element
        self.tail = walk
        self.tail.next = None
        
        return ret_element

        
    
    def delete_first(self): # Big O(1)
        if self.is_empty():
            raise Empty('DeQue is empty')
        ret_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        return ret_element
        
    
    def first(self):
        if self.is_empty():
            raise Empty('DeQue is empty')
        return self.head.element
    
    def last(self):
        if self.is_empty():
            raise Empty('DeQue is empty')
        return self.tail.element


    def __str__(self):
        if self.is_empty():
            raise Empty('DeQue is empty')
        
        ret_str = 'The DeQue (Front - Back): '
        walk = self.head
        while walk != None:
            ret_str += str(walk.element + ' ')
            walk = walk.next
        return ret_str

if __name__ == "__main__":
    print("--- test cases ---")

    Linked_DeQue = LinkedDeQue()
    Linked_DeQue.add_first('a')
    Linked_DeQue.add_first('c')
    Linked_DeQue.add_first('d')
    Linked_DeQue.add_last('z')
    print(Linked_DeQue)

    print(Linked_DeQue.delete_last())
    print(Linked_DeQue.delete_first())
    print(Linked_DeQue.first())
    print(Linked_DeQue.delete_last())
    print(Linked_DeQue.first())
    print(Linked_DeQue.last())

    print(Linked_DeQue)