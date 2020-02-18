class STACK:
    # LIFO - Last in fyrst out
    def __init__(self):
        self.a_list = []

    def push(self, value):
        self.a_list.append(value)

    def pop(self):
        val = self.a_list[-1]
        del self.a_list[-1]
        return val
    
    def __str__(self):
        return str(self.a_list)

class QUEUE:
    # FIFO - First in first out
    def __init__(self):
        self.a_list = []

    def add(self, value):
        self.a_list.append(value)

    def remove(self):
        val = self.a_list[0]
        del self.a_list[0]
        return val
    
    def __str__(self):
        return str(self.a_list)

class DEQUE:
    # Both FIFO and LIFO
    def __init__(self):
        self.a_list = []

    def pop_front(self):
        val = self.a_list[0]
        del self.a_list[0]
        return val

    def pop_back(self):
        val = self.a_list[-1]
        del self.a_list[-1]
        return val

    def push_front(self, value):
        self.a_list.insert(0, value)

    def push_back(self, value):
        self.a_list.append(value)
    
    def __str__(self):
        return str(self.a_list)

a_stack = DEQUE()

a_stack.push_back(1)
a_stack.push_front("hello")
a_stack.push_back(2)
a_stack.push_back(5)
a_stack.push_front(5)
a_stack.push_front(5)

a_1 = a_stack.pop_back()
print("Item popped:", a_1)
print(a_stack)
a_1 = a_stack.pop_front()
print("Item popped:", a_1)
print(a_stack)