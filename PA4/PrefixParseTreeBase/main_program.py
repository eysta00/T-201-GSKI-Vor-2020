
import sys
from enum import Enum

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2

class Tokenizer:
    def __init__(self, str_statement):
        self.statement = str_statement
        self.position = 0

    def get_next_token(self):
        i = self.position
        while i < len(self.statement) and self.statement[i] != " ":
            i += 1
        ret_val = self.statement[self.position:i]
        self.position = i + 1
        return ret_val

def prefix_parser_recursive(tokenizer):
    token = tokenizer.get_next_token()
    # print(token) # debug line
    if token.isdigit():
        return int(token)
    elif token == "+":
        return prefix_parser_recursive(tokenizer) + prefix_parser_recursive(tokenizer)
    elif token == "-":
        return prefix_parser_recursive(tokenizer) - prefix_parser_recursive(tokenizer)
    elif token == "*":
        return prefix_parser_recursive(tokenizer) * prefix_parser_recursive(tokenizer)
    elif token == "/":
        val1 = prefix_parser_recursive(tokenizer)
        val2 = prefix_parser_recursive(tokenizer)
        if(val2 == 0):
            raise DivisionByZero
        return val1 / val2
    return 0

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class PrefixParseTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.format = OutputFormat.PREFIX

    def _load_statement_recur(self, tokenizer):
        token = tokenizer.get_next_token()
        token_node = BinaryTreeNode(token)
        if self.root == None:
            self.root = token_node
        
        # print(token) # debug line
        
        if token.isdigit() or token == 'x':
            self.size += 1
            return token_node
        elif token in '+-*/':
            token_node.left = self._load_statement_recur(tokenizer)
            token_node.right = self._load_statement_recur(tokenizer)
            self.size += 1
            return token_node

    def load_statement_string(self, statement):
        ''' It takes in a prefix statement as a string, parses the
            string (you can use the tokenizer class from the recursive prefix parser) and builds a
            statement tree. '''
        tokenizer = Tokenizer(statement)
        self._load_statement_recur(tokenizer)     

    def set_format(self, out_format):
        self.format = out_format

    def root_value(self, node = None):
        if node == None:
            node = self.root

        if node.data.isdigit():
            return int(node.data)
        elif node.data == "+":
            return self.root_value(node.left) + self.root_value(node.right)
        elif node.data == "-":
            return self.root_value(node.left) - self.root_value(node.right)
        elif node.data == "*":
            return self.root_value(node.left) * self.root_value(node.right)
        elif node.data == "/":
            val1 = self.root_value(node.left)
            val2 = self.root_value(node.right)
            if(val2 == 0):
                raise DivisionByZero
            return val1 / val2
        else:
            raise UnknownInTree
        return 0
    
    def _simplify_tree_recur(self, node):
        if node.left.data.isdigit() and node.right.data.isdigit():
            value = self.root_value(node)
            node.data = str(value)
            node.left = None
            node.right = None
            return True
        elif node.right.data in '*/+-':
            is_simplefied = self._simplify_tree_recur(node.right)
            if node.left.data == 'x' or node.right.data == 'x':
                return False
            elif is_simplefied:
                is_simplefied = self._simplify_tree_recur(node)
                return is_simplefied

        elif node.left.data in '*/+-':
            is_simplefied = self._simplify_tree_recur(node.left)
            if node.left.data == 'x' or node.right.data == 'x':
                return False
            elif is_simplefied:
                is_simplefied = self._simplify_tree_recur(node)
                return is_simplefied

        if node.right == None or node.left == None:
            return True
            
        if node.right.data == 'x' or node.left.data == 'x':
            return False
        

    def simplify_tree(self):

        return self._simplify_tree_recur(self.root)
        
    def solve_tree(self, root_value):
        pass

    def _print_prefix_recur(self, node):
        ''' Recrusive preorder printer '''
        if node == None:
            return ""
        ret_str = ""
        if node.data.isdigit() or node.data == "x":
            ret_str = node.data
        else:
            ret_str += node.data + " " + self._print_prefix_recur(node.left) + " " + self._print_prefix_recur(node.right)
        return ret_str

    def _print_infix_recur(self, node):
        ''' recursive inorder printer '''
        if node == None:
            return ""
        
        ret_str = ""
        
        if node.data.isdigit() or node.data == "x":
            ret_str = node.data
        else:
            ret_str += "(" + self._print_infix_recur(node.left) + " " + node.data + " " + self._print_infix_recur(node.right) + ")"

        return ret_str

    def _print_postfix_recur(self, node):
        ''' recursive postorder printer '''
        if node == None:
            return ""
        
        ret_str = ""

        if node.data.isdigit() or node.data == "x":
            ret_str = node.data
        else:
            ret_str += self._print_postfix_recur(node.left) + " " + self._print_postfix_recur(node.right) + " " + node.data

        return ret_str

    def __str__(self):
        if self.format == OutputFormat.PREFIX:
            ret_str = str(self._print_prefix_recur(self.root))
        elif self.format == OutputFormat.POSTFIX:
            ret_str = str(self._print_postfix_recur(self.root))
        elif self.format == OutputFormat.INFIX:
            ret_str = str(self._print_infix_recur(self.root))
        return ret_str


# This is a tester function to test that
# the output and/or error message from the
# prefix_tree operations are correct.
def test_prefix_parser(str_statement, solve = False, root_value = 0):

    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")


if __name__ == "__main__":
    # prefix_tree = PrefixParseTree()
    # prefix_tree.load_statement_string('* - * - - 5 0 - 6 4 + 7 4 - + * 6 2 0 - 2 6 + * 4 - + 0 0 3 * 3 + 2 7')
    # print(prefix_tree.root.data)
    # print(prefix_tree.size)
    # print("PREFIX: " + str(prefix_tree))
    # prefix_tree.set_format(OutputFormat.INFIX)
    # print("INFIX: " + str(prefix_tree))
    # prefix_tree.set_format(OutputFormat.POSTFIX)
    # print("POSTFIX: " + str(prefix_tree))
    # #print(prefix_tree.root_value())
    # prefix_tree.simplify_tree()
    # prefix_tree.set_format(OutputFormat.INFIX)
    # print("INFIX: " + str(prefix_tree))
    # prefix_tree.set_format(OutputFormat.PREFIX)
    # print("PREFIX: " + str(prefix_tree))

    
    org_out = sys.stdout
    fout = open(sys.path[0] + "/parse_out.txt", "w+")
    sys.stdout = fout
    f = open(sys.path[0] + "/prefix_statements.txt", "r")
    previous_line = None
    for line in f:
        some_split = line.split()
        if some_split[0] == "solve":
            test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
        test_prefix_parser(line.strip())
        previous_line = line
    f.close()
    sys.stdout = org_out
    fout.close()
