class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def palindrome(head, list_copy = None):
    if list_copy == None:
        if head == None or head.next == None: # check á minna eða sama og 1
            return True

        list_copy = head # geyma fremsta hausinn (copy)
    elif head.next == None: 
        return list_copy.next, True

    new_list_copy, pal_bool = palindrome(head.next, list_copy)
    
    if pal_bool == True and head.data == new_list_copy.data:
        pal_bool = True # check á eins data
    else:
        pal_bool = False
   
   
    if head == list_copy: # Bera bendla saman
        return pal_bool  # skila bool á seinsta kalli

    return new_list_copy.next, pal_bool
    

if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")