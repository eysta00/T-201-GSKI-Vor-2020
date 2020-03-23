class Item:
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

    def __eq__(self, other):
        return self.key == other.key
    
    def __ne__(self, other):
        return not(self.key == other.key)
    
    def __lt__(self, other):
        return self.key < other.key
    
class LinkedNode:
    def __init__(self, _object = None, _next = None):
        self.object = _object
        self.next = _next

class Map:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data): # Má merga # O(1)
        ''' Create a new key with data '''
        new_node = LinkedNode(Item(key, data),self.head)
        self.head = new_node
        self.size += 1
        return

    def __len__(self):
        return self.size

    def __str__(self): # O(n)
        ret_str = "{"
        counter = 0
        for item in self:
            counter += 1
            if counter == self.size:
                ret_str += str(item.key) + ":" + str(item.data) + "}"
            else:
                ret_str += str(item.key) + ":" + str(item.data) + ", "
        return ret_str
    
    def update(self, k, data): # Má merga # O(n)
        ''' Update data of a key '''
        for item in self:
            if item.key == k:
                item.value = data
    
    def __setitem__(self, key, data): # O(n)
        ''' Merged version '''
        if key in self:
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, k): # Return data
        ''' Return data of a key '''
        for item in self:
            if k == item.key:
                return item.data
        raise KeyError('Key Error: ' + str(k))

    def __delitem__(self, key):
        node = self.head
        while node != None:
            if node.next.object.key == k:
                node.next = node.next.next
                self.size -= 1
                return

            node = node.next
        raise KeyError('Key Error: ' + str(k))

    def __iter__(self):
        node = self.head
        while node != None:
            yield node.object
            node = node.next

    def remove(self, k):
        ''' Remove a key '''
        node = self.head
        while node != None:
            if node.next.object.key == k:
                node.next = node.next.next
                self.size -= 1
                return

            node = node.next
        raise KeyError('Key Error: ' + str(k))

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

if __name__ == "__main__":
    My_Dict = Map()
    My_Dict.insert(4, "Ass")
    My_Dict.insert(1, "Fart")
    My_Dict.insert(2, "Gas")
    My_Dict.insert(5, "Larp")
    print(My_Dict)
    print(My_Dict[4])
    My_Dict.remove(6)
    print(My_Dict)