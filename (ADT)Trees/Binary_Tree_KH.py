class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        ''' Have to know where the tree begings '''
        self.root = None
    
    def _populate_tree_recur(self, level = 0):
        ''' Recursive way to input data into tree '''
        data_str = input()
        if data_str == '':
            return None
        level += 1
        print(level*"   |"+"--LEFT :", end=" ")
        left = self._populate_tree_recur(level)
        print(level*"   |"+"--RIGHT :", end=" ")
        right = self._populate_tree_recur(level)
        return BinaryTreeNode(data_str, left, right)

    def populate_tree(self):
        ''' Initialize recursive populate tree '''
        print("ROOT :", end=" ")
        self.root = self._populate_tree_recur()
    

    def _print_preorder_recur(self, node):
        ''' Recrusive preorder printer '''
        if node == None:
            return
        print(str(node.data), end = " ")
        self._print_preorder_recur(node.left)
        self._print_preorder_recur(node.right)
    
    def print_preorder(self):
        ''' initialize recrusive preorder '''
        print("Preorder:",end="")
        self._print_preorder_recur(self.root)
        print("")
        
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
    
    def _print_postorder_recur(self, node):
        ''' recursive postorder printer '''
        if node == None:
            return
        self._print_postorder_recur(node.left)
        self._print_postorder_recur(node.right)
        print(str(node.data), end = " ")
    
    def print_postorder(self):
        ''' initialize recursive postorder '''
        print("Postorder:",end="")
        self._print_postorder_recur(self.root)
        print("")

    def _value_counter_recur(self, value, node, counter = 0):
        ''' Recursive way to find the number of specific values in a tree '''
        if node == None:
            return counter
        # The case for bin-tree
        counter = self._value_counter_recur(value, node.left, counter)
        counter = self._value_counter_recur(value, node.right, counter)

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
        self._replace_val_recur(node.left, val_1, val_2)
        self._replace_val_recur(node.right, val_1, val_2)

        if node.data == val_1:
            node.data = val_2
        return
    
    def replace_val(self):
        print("Value repalcer")
        val_1 = input("The value to be replaced: ")
        val_2 = input("The value that takes it's place: ")
        self._replace_val_recur(self.root, val_1, val_2)
        self.print_postorder()   

if __name__ == "__main__":
    bt = BinaryTree()
    bt.populate_tree()
    bt.count_val()
    bt.print_preorder()
    bt.print_inorder()
    bt.print_postorder()
    bt.replace_val()