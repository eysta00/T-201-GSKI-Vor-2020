
class ArrayDeque():
    def __init__(self):
        self.capacity = 4
        self.back = 0
        self.front = 0
        self.arr = [None] * self.capacity
        self.size = 0

    def push_back(self, value):
        """Takes a parameter and adds its value to the back of the deque"""
        if self.capacity == self.size:
            self.__resize()
        self.arr[self.size] = value

    def push_front(self, value):
        pass

    def pop_front(self):
        pass

    def pop_back(self):
        pass
    
    def get_size(self):
        pass
    
    def __resize(self):
        self.capacity += self.capacity
        new_arr = [None] *(self.capacity)
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
