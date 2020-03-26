class Error(Exception):
    pass
class NotFoundException(Error):
    pass

class ItemExistsException(Error):
    pass

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

class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self): # (Helper method) (yeilds the object, not the node)
        node = self.head
        while node != None:
            yield node.object
            node = node.next

    def __str__(self): # O(n) (Helper method)
        ret_str = "{"
        counter = 0
        for item in self:
            counter += 1
            if counter == self.size:
                ret_str += str(item.key) + ":" + str(item.data) + "}"
            else:
                ret_str += str(item.key) + ":" + str(item.data) + ", "
        return ret_str
    

    def __setitem__(self, key, data): # O(n)
        ''' Merged version (both update and insert) '''
        if key in self:
            self.update(key, data)
        else:
            self.insert(key, data)

    def insert(self, key, data): # O(n)
        ''' Create a new key with data '''
        if key in self:
            raise ItemExistsException('The key ' + str(key) + ' is already in the list')
        new_node = LinkedNode(Item(key, data),self.head)
        self.head = new_node
        self.size += 1
    
    def update(self, k, value): # O(n)
        ''' Update data of a key '''
        for item in self:
            if item.key == k:
                item.data = value
                return
        raise NotFoundException('The key ' + str(k) + ' was not found')

    def __getitem__(self, k): # Return data
        ''' Return data of a key '''
        for item in self:
            if k == item.key:
                return item.data
        raise NotFoundException('The key ' + str(k) + ' was not found')

    def find(self, k):
        return self[k]

    def remove(self, k):
        ''' Remove a key '''
        if k not in self:
            raise NotFoundException("Key not found")
        if self.head.object.key == k:
            self.head = self.head.next
            self.size -= 1
            return

        node = self.head
        while node != None:
            if node.next.object.key == k:
                node.next = node.next.next
                self.size -= 1
                return
            node = node.next
    

    def contains(self, key):
        if key in self:
            return True
        else:
            return False

    def __contains__(self, key): # Nota þetta því það er cool
        try:
            self[key]
            return True
        except NotFoundException:
            return False

if __name__ == "__main__":
    print("Private tests of Bucket class")
    this_map = Bucket()
    this_map.insert("a", 1)
    this_map.insert("b", 1)
    this_map.insert("c", 1)
    this_map["d"] = 3
    this_map["b"] = 2
    print(this_map)
    print(this_map.find("d"))
    this_map.remove("d")
    print(this_map)
    this_map.remove("b")
    print(this_map)
    this_map.remove("a")
    print(this_map)
