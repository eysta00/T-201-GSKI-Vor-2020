from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, type: str):
        if type == "array":
            self.PEZ = ArrayDeque()
        elif type == "linked"
            self.PEZ = LinkedList()
        
    def push(self, val):
        self.PEZ.push_front(val)

    def pop(self):
        if self.PEZ.is_empty():
            return None
        else:
            return self.PEZ.pop_front()

    def get_size(self):
        return self.PEZ.get_size()
