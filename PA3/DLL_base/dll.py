
class Node:
    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element, prev, next):
        self._element = element
        self._next = next
        self._prev = prev

class DLL:
    def __init__(self):
        self._size = 0
        self._current = None
        self._header = Node(None, None, None)
        self._trailer = Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header

    def __len__(self):
        return self._size
    
    def __str__(self):
        return_str = ''
        walk = self._header._next
        while walk._element != None:
            return_str += walk._element + ' '
            walk = walk._next
        return return_str
    
    def reverse_str(self):
        return_str = ''
        walk = self._trailer._prev
        while walk._element != None:
            return_str += walk._element + ' '
            walk = walk._prev
        return return_str
    
    def is_empty(self):
        return self._size == 0
    
    def insert(self, value):
        if self.is_empty():
            new_node = Node(value, self._header, self._trailer)
            self._trailer._prev = new_node
            self._header._next = new_node
            self._current = new_node
            self._size += 1
        else:
            new_node = Node(value, self._current._prev, self._current)
            self._current._prev._next = new_node
            self._current._prev = new_node

            self._current = new_node
            self._size += 1

    def remove(self):
        if not self.is_empty():
            next_node = self._current._next
            prev_node = self._current._prev
            next_node._prev = prev_node
            prev_node._next = next_node
            old_node = self._current
            
            self._current = next_node
            old_node._element = old_node._next = old_node._prev = None # garbage

            if self._current._element == None:
                self._current = self._trailer._prev # ef að síðastan nóðan er hent þá


    def get_value(self):
        return self._current._element
    
    def move_to_next(self):
        if self._current._element != None:
            if self._current._next._element != None:
                self._current = self._current._next
    
    def move_to_prev(self):
        if self._current._element != None:
            if self._current._prev._element != None:
                self._current = self._current._prev

    def move_to_pos(self, position):
        pos_counter = 0
        walk = self._header._next
        while pos_counter <= position and walk._element != None:
            walk = walk._next
            pos_counter += 1
        
        self._current = walk

    def remove_all(self, value):
        
    
    def reverse(self):
        pass

    def sort(self):
        pass


if __name__ == "__main__":
    dll_ = DLL()
    dll_.insert('a')
    print(dll_)
    print(dll_._current._element)
    dll_.insert('b')
    print(dll_)    
    print(dll_._current._element)
    dll_.insert('c')
    print(dll_.reverse_str())
    print(dll_)
    print(dll_._current._element, "current")
    dll_.move_to_next()
    print(dll_._current._element)
    
    dll_.remove()
    
    print(dll_)
    print(dll_._current._element)


