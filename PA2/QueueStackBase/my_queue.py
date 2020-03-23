from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, type: str):
        if type == "array":
            self.my_queue = ArrayDeque()
        elif type == "linked":
            self.my_queue = LinkedList()

    def add(self, val):
        self.my_queue.push_back(val)

    def remove(self):
        if self.my_queue.is_empty():
            return None
        else:
            return self.the_queue.pop_front()
    
    def get_size(self):
        return self.my_queue.get_size()
    
