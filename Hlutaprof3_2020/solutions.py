
# Implement helper classes here

class LRCMap:
    class Node:
        def __init__(self, data = None, left = None, center = None, right = None):
            self.data = data
            self.left = left
            self.center = center
            self.right = right

    def __init__(self, build = False):
        self.build = build
        self.root = None
        if build == False:
            self._build_tree()

    def _build_tree_node(self, node):
        left = Node()
        center = Node()
        right = Node()
        node.left = left
        node.right = right
        node.center = center
        _build_tree_node(node.left)
        _build_tree_node(node.center)
        _build_tree_node(node.right)


    def _build_tree(self):
        curr_node = Node()
        self.root = curr_node
        for _ in range(9): # Er bara að gera vinstri endalaust... vitlaust
            _build_tree_node(curr_node)
            curr_node = curr_node.left

        curr_node = self.root
        for _ in range(9):
            _build_tree_node(curr_node)
            curr_node = curr_node.center
        
        curr_node = self.root
        for _ in range(9):
            _build_tree_node(curr_node)
            curr_node = curr_node.right
        
        self.build = True


    def put_data(self, key, data):
        pass

    def get_data(self, key): # returns data for that key or None if non-existant
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING


class HashMap:
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
       # self.hash_table = [ [ ] for _ in range(self.array_length) ]
       # self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def __setitem__(self, key, data): # overrides/updates if already there
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def __getitem__(self, key): # returns data - returns None if nothing there
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def __len__(self):
        return 0


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))


    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
