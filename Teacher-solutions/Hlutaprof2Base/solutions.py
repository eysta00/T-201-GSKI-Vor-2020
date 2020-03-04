
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

def is_ordered(head):
    if head.next == None:
        return True
    
    bool_val = is_ordered(head.next)
    bool_val &= head.data <= head.next.data 

    return bool_val


class DLL_List:

    class Node:
        def init (self, element, prev, next): 
            self._element = element 
            self._prev = prev 
            self._next = next

    def init (self):
        self._header = self. Node(None, None, None)
        self._trailer = self. Node(None, None, None)
        self._header._next = self. trailer
        self._trailer._prev = self. header
        self._size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, pre, nex):
        newest = self. Node(e, pre, nex) # linked to neighbors
        pre._next = newest
        nex._prev = newest
        self. size += 1
        return newest
    
    def delete_node(self, node):
        pre = node._prev 
        nex = node._next
        pre._next = nex
        nex._prev = pre
        self.size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
    print(is_ordered(head))
    head = SLL_Node(5, SLL_Node(4, SLL_Node(3, SLL_Node(2, SLL_Node(1)))))
    print(str(head))
    print(is_ordered(head))
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(3, SLL_Node(5)))))
    print(str(head))
    print(is_ordered(head))