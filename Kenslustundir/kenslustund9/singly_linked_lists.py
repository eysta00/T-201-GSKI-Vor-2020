class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def chop_off(self, head):
        self.head.data = None
    
    def chop_back(self, tail):
        self.tail.data = None
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None: # tómur listi
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def get_size(self, head):
        self.size += 1
        if head == None:
            return size
        else:
            get_size(head.next)
    
    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str


def push_front(head, data):
    new_node = Node(data, head)
    return new_node

def print_list(head):
    if head != None:
        print(head.data)
        print_list(head.next)





head = Node()
head.data = "string 1"
for i in range (2,6):
    head = push_front(head, "string " + str(i))


print_list(head)

listinn = LinkedList()
for i in range(1,6):
    listinn.push_back("hello " + str(i))
    if i == 2:
        listinn.chop_off(listinn.tail)

print(listinn)

listi2 = LinkedList()
for i in range(1,10):
    listi2.push_back("kappa " + str(i))

listi2.get_size(listi2.head)
print(listi2.size)