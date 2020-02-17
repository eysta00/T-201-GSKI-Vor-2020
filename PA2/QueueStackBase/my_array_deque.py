
class ArrayDeque():
    def __init__(self):
        self._capacity = 4
        self._first = 0
        self._last = 0
        self._arr = [None] * self._capacity
        self._size = 0

    def push_back(self, value):
        """Takes a parameter and adds its value to the back of the deque"""
        if self._capacity == self._size:
            self._resize()
        self._arr[self._last] = value
        self._last = (self._last + 1) % self._capacity
        self._size += 1

    def push_front(self, value):
        """Takes a parameter and adds its value to the front of the deque"""
        if self._capacity == self._size:
            self._resize()
        self._first = (self._first - 1) % self._capacity
        self._arr[self._first] = value
        self._size += 1

    def is_empty(self):
        """Returns if the string is empty or not (True/False)"""
        return self._size <= 0

    def pop_back(self):
        """removes the item from the back of the deque and returns its value"""
        """If the deque is empty, return None"""
        if self.is_empty():
            return None
        else:
            self._last = (self._last - 1) % self._capacity
            self._size -= 1
            return self._arr[self._last]

    def pop_front(self):
        """removes the item from the front of the deque and returns its value"""
        """If the deque is empty, return None"""
        if self.is_empty():
            return None
        else:
            placeholder = self._arr[self._first]
            self._first = (self._first + 1) % self._capacity
            self._size -= 1
            return placeholder

    def get_size(self):
        """Returns the size of the deque"""
        return self._size

    def __len__(self):
        return self._size

    def _resize(self):
        """Double the size of the array"""
        """Optional to leave the first space empty"""
        old = self._arr
        self._arr = [None] * (self._capacity*2)
        self._capacity *= 2 
        walk = self._first
        for k in range(self._size):
            self._arr[k] = old[walk]
            walk += 1
            walk %= len(old)
        self._first = 0
        self._last = self._size
    
    def __str__(self):
        a_str = ""
        if self.is_empty():
            return a_str
        if self._last == 0 or self._last > self._first:
            for i in range(self._first, self._first + self._size - 1):
                a_str += str(self._arr[i]) + " "
            a_str += str(self._arr[self._last -1])
        else:
            for i in range(self._first, self._capacity):
                a_str += str(self._arr[i]) + " "
            for i in range(self._last - 1):
                a_str += str(self._arr[i]) + " "
            a_str += str(self._arr[self._last -1])
        return a_str