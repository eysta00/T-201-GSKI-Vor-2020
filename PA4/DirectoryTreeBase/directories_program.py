class TreeNode:
    def __init__(self, name = "", parent = None):
        self.name = name
        self.children = [] # Python Built in
        self.parent = parent

class GeneralTree:
    def __init__(self, root):
        self.root = root
        self.current = self.root
    
    def check_is_in(self,name):
        ''' Returns a bool '''
        for child in self.current.children:
            if child.name == name:
                return True
        return False
    
    def find_node(self, name):
        for child in self.current.children:
            if child.name == name:
                return child
        return None

    def mkdir(self, name):
        if self.check_is_in(name):
            return True
        new_dir = TreeNode(name, self.current)
        self.current.children.append(new_dir)# Python Built in
        return False

    def cd_up(self):
        if self.current.parent == None:
            return True
        else:
            self.current = self.current.parent
            return False

    
    def cd_down(self, name):
        for node in self.current.children:
            if name == node.name:
                self.current = node
                return False
        return True
    
    
    def ls(self):
        ret_list = []
        for node in self.current.children:
            ret_list.append(node.name) # Python Built in
        ret_list.sort() # Python Built in
        for name in ret_list:
            print(name)


    def rm(self, name):
        if self.check_is_in(name):
            self.current.children.remove(self.find_node(name)) # Python Built in
            return True
        return False

    
        

    
    

'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.
'''


def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)
    dir_tree = GeneralTree(tree)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            # command[1] is the name of the subdirectory that should be made here
            if dir_tree.mkdir(command[1]):
                print("  Subdirectory with same name already in directory")

        elif command[0] == "ls":
            print("  Listing the contents of current directory:  " + str(dir_tree.current.name)) # Add the name of the directory here
            dir_tree.ls()

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
            # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                if dir_tree.cd_up():
                    print("Exiting directory program")
                    break
                    
            else:
                if dir_tree.cd_down(command[1]):
                    print("  No folder with that name exists")
            print("  current directory: " + str(dir_tree.current.name)) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if dir_tree.rm(command[1]):
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
