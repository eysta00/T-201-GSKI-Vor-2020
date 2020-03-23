class HeapNode:
    def __init__(self, priority, data = None, parent = None, left = None, right = None):
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class PriorityQueue:
    def __init__(self):
        self.root = None
        self.last_node = None

    def add(self, priority, value): # Is tékkar hvort þetta sé sama minnisvæðið en == skoða gögnin
        if self.root == None:
            self.last_node = self.root = HeapNode(priority, value)
        elif self.last_node.parent != None and self.last_node is self.last_node.parent.left:

            self.last_node.parent.right = HeapNode(priority, value, self.last_node.parent)
            self.last_node = self.last_node.parent.right
        
        else:
            next_to_add = self.last_node

            while next_to_add is not self.root and next_to_add is next_to_add.parent.right:
                next_to_add = next_to_add.parent
            
            if next_to_add is not self.root:
                next_to_add = next_to_add.parent.right
            
            while next_to_add.left != None:
                next_to_add = next_to_add.left
            
            next_to_add.left = HeapNode(priority, value, next_to_add)
            self.last_node =next_to_add.left
        
        # bubble up
        node = self.last_node
        while node.parent != None and node.priority < node.parent.priority:
            self.swap_values(node,node.parent)
            node = node.parent 

    def remove(self):
        if self.last_node == None:
            return None
        ret_val = self.root.data
        if self.last_node is self.root:
            self.last_node = self.root = None
            return ret_val
        self.swap_values(self.last_node, self.root)
        if self.last_node is self.last_node.parent.right:
            self.last_node = self.last_node.parent.left
            self.last_node.parent.right = None
        else:
            self.last_node = self.last_node.parent
            self.last_node.left = None
            # Go up
            while self.last_node is not self.root and self.last_node is self.last_node.parent.left:
                self.last_node = self.last_node.parent
            # If not at root
            if self.last_node is not self.root:
                self.last_node = self.last_node.parent.left
            
            while self.last_node.right != None:
                self.last_node = self.last_node.right
            
            #Bubble down
            while node.left != None:
                if node.right != Noen and node.right.priority < node.priority:
                    if node.left.priority < node.right.priority:
                        self.swap_values(node, node.right)
                    else:
                        self.swap_values(node, node.right)
                        node = ndoe.right
                elif node.left.priority < node.priority:

                    self.swap_values(node, node.left)
                    node = node.left
                else:
                    break
            return ret_val
        
    def is_empty(self):
        return self.root == None
        
    def swap_values(node, parent):
        data_to_swap = node.data
        node.data = parent.data
        parent.data = data_to_swap

    def _print_inorder_recur(self, node):
        ''' recursive inorder printer '''
        if node == None:
            return
        self._print_inorder_recur(node.left)
        print(str(node.data), end = " ")
        self._print_inorder_recur(node.right)
    
    def print_inorder(self):
        ''' initialize inorder printer '''
        print("Inorder:",end="")
        self._print_inorder_recur(self.root)
        print("")

if __name__ == "__main__":
    PQ = PriorityQueue()
    PQ.add(1, "a")
    PQ.add(2, "b")
    PQ.add(5, "l")
    PQ.add(3, "v")
    PQ.add(8, "x")
    PQ.add(6, "g")
    PQ.print_inorder()