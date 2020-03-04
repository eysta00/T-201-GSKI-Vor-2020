class GeneralTreeNode:
    def __init__(self, data = None):
        self.data = data
        self.children = []

class GeneralTree:
    def __init__(self):
        ''' Need to know what node is the begning'''
        self.root = None
    
    def _populate_tree_recur(self, level = 0):
        ''' A Recursive way to input data into general tree '''
        data_str = input()
        if data_str == '':
            return None
        level += 1
        
        node = GeneralTreeNode(data_str)
        while True:  
            print(level*"   |"+"--NODE :", end=" ")
            child_node = self._populate_tree_recur(level)
            if child_node == None:
                break
            node.children.append(child_node)

        return node
        
    def populate_tree(self):
        ''' Initialize recursive population '''
        print("ROOT :", end=" ")
        self.root = self._populate_tree_recur()
    
    def _print_preorder_recur(self, node):
        ''' Recrusive way to print all data in a pre-order (First itself, then children) '''
        if node == None:
            return
        print(str(node.data), end = " ")
        for child_node in node.children:
            self._print_preorder_recur(child_node)
    
    def print_preorder(self):
        ''' Initalize the recursive preorder '''
        self._print_preorder_recur(self.root)
        print("")
    
    def _print_postorder_recur(self, node):
        ''' Recrusive way to print all data in a post-order (First children, then itself) '''
        if node == None:
            return
        for child_node in node.children:
            self._print_postorder_recur(child_node)
        print(str(node.data), end = " ")
    
    def print_postorder(self):
        ''' Initalize the recursive postorder '''
        self._print_postorder_recur(self.root)
        print("")
    
    def _value_counter_recur(self, value, node, counter = 0):
        ''' Recursive way to find the number of specific values in a tree '''
        if node == None:
            return counter
        # the case for gen-tree
        for child_node in node.children:
            counter = self._value_counter_recur(value, child_node, counter)
        if node.data == value:
            counter += 1
        return counter

    def count_val(self):
        ''' Initalize recursive count '''
        print("Value Counter, input a value and I \nwill find how many there are in the tree")
        value = input("Insert: ")
        num = self._value_counter_recur(value, self.root)
        print(value, "Appeared", num, "Times")
    
    def _replace_val_recur(self, node, val_1, val_2):
        if node == None:
            return
        for child_node in node.children:
            self._replace_val_recur(child_node, val_1, val_2)
        if node.data == val_1:
            node.data = val_2
        return
    
    def replace_val(self):
        print("Value repalcer")
        val_1 = input("The value to be replaced: ")
        val_2 = input("The value that takes it's place: ")
        self._replace_val_recur(self.root, val_1, val_2)
        self.print_preorder()    



if __name__ == "__main__":
    gt = GeneralTree()
    gt.populate_tree()
    gt.count_val()
    print("Postorder: ", end=" ")
    gt.print_postorder()
    print("Preorder: ", end=" ")
    gt.print_preorder()
    gt.replace_val()
