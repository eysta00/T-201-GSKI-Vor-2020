from time import time
import random

def power (base, power):
    return_val = base ** power
    #return_val = 1
    #for _ in range(power):
    #    return_val *= base
    return return_val

def multi (num, multicator):
    return_val = 0
    if num > multicator:
        for _ in range(multicator):
            return_val += num
    else:
        for _ in range(num):
            return_val += multicator
    
    return return_val

def random_insertion (list_size):
    lst = [0] * list_size
    for i in range(len(lst)):
        if i == 1:
            num = (7 * 3 + 4) % 9
            lst[0] = num
        else:
            num = (7 * lst[i - 1] + 4) % 9
            lst[i] = num
    return lst

def print_list (a_list):
    print_str = ""
    some_num = len(a_list) - 1
    for i in range(len(a_list)):
        element = str(a_list[i-1])
        print_str += element
        if i != some_num:
            print_str += ", "
    return print_str

def inc_num_at_random_index(a_list):
    rand_int = random.randint(0,len(a_list)) - 1
    a_list[rand_int] = a_list[rand_int] + 1
    return a_list

def switch_items_in_list(list_lenght):
    a_list = [1, 2, 3] * list_lenght
    list_lenght = list_lenght * 3 - 1
    a, b = a_list[0], a_list[1]
    a_list[0], a_list[1] = b, a
    c = random.randint(0, list_lenght)
    d = random.randint(0, list_lenght)
    switch_1, switch_2 = a_list[d], a_list[c]
    a_list[d], a_list[c] = switch_2, switch_1

    return a_list

def ordered_insert():
    a_list = [0] * 5
    for i in range(len(a_list)):
        rand_num = random.randint(0, 10)
        a_list[i] = rand_num
    for i in range(len(A)):
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 

    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
    return a_list

a_list = random_insertion(10)
#start_time = time()
string = ordered_insert()
#end_time = time()
print(string)
#print(end_time - start_time)
