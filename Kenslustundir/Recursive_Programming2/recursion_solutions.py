
def power(base, exp):
    if exp == 1:
        return base
    return base * power(base, exp - 1)

def mult_recur(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -a + mult_recur(a, b + 1)
    else:
        return a + mult_recur(a, b - 1)
def multiply(a, b):
    if abs(a) < abs(b):
        return mult_recur(b, a)
    else:
        return mult_recur(a, b)

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)

def nat_recur(n):
    if n > 0:
        return nat_recur(n - 1) + " " + str(n)
    return ""
def natural(n):
    print(nat_recur(n))

def sum_of_digits(x):
    if x < 10:
        return x
    return (x % 10) + sum_of_digits(x // 10)

def fibon_recur(counter, current, previous):
    if counter <= 2:
        return 1
    return current + fibon_recur(counter - 1, current + previous, current)
def fibonacci(n):
    if n <= 1:
        return n
    return fibon_recur(n, 1, 0)

def Ackermann(m, n):
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return Ackermann(m - 1, 1)
    else:
        return Ackermann(m - 1, Ackermann(m, n - 1))

def linear_search(list, value):
    if len(list) == 0:
        return False
    if list[0] == value:
        return True
    return linear_search(list[1:], value)

def count_instances(list, value):
    if len(list) == 0:
        return 0
    ret_val = count_instances(list[1:], value)
    if list[0] == value:
        ret_val += 1
    return ret_val

def are_duplicates(list):
    if len(list) == 0:
        return False
    tail = list[1:]
    is_duplicate = linear_search(tail, list[0])
    if is_duplicate:
        return True
    return are_duplicates(tail)

def remove_duplicates(list):
    if len(list) == 1:
        return list
    head = list[0]
    tail = list[1:]
    is_duplicate = linear_search(tail, head)
    if is_duplicate:
        return remove_duplicates(tail)
    return [head] + remove_duplicates(tail)

def is_prefix(prefix, a_str):
    if len(prefix) == 0:
        return True
    elif len(a_str) == 0:
        return False
    if prefix[0] != a_str[0]:
        return False
    return is_prefix(prefix[1:], a_str[1:]) # recur and move forward on both strings

def is_substring(substring, a_str):
    if len(a_str) == 0:
        if len(substring) == 0:
            return True
        else:
            return False
    if is_prefix(substring, a_str): #if its in the beginning of the string, cool
        return True
    return is_substring(substring, a_str[1:]) #otherwise recur but only move forward on main string, substring is still the same

def is_in_string(a_str, c):
    if len(a_str) == 0:
        return False
    if a_str[0] == c:
        return True
    return is_in_string(a_str[1:], c)

def x_ish(a_str, x):
    if len(x) == 0:
        return True
    if is_in_string(a_str, x[0]):
        return x_ish(a_str, x[1:])
    return False

def palindrome_recursive(forward_string, reverse_string):
    if len(forward_string) == 0:    #This works because I only ever call this with equally long strings
        return True                 #Otherwise we would also have to check for reverse_string
    if forward_string[0] != reverse_string[-1]:
        return False
    return palindrome_recursive(forward_string[1:], reverse_string[:-1])


def palindrome(a_str):
    return palindrome_recursive(a_str, a_str)

print("\nPOWER\n")

print(power(2, 2))
print(power(1, 5))
print(power(5, 1))
print(power(3, 3))
print(power(6, 2))

print("\nMULTIPLY\n")

print(multiply(4, 9))
print(multiply(100, 100))
print(multiply(3, 7))
print(multiply(29, 11))
print(multiply(5, 2))
print(multiply(-4, 9))
print(multiply(-100, -100))
print(multiply(3, -7))
print(multiply(-29, 11))
print(multiply(5, -2))

print("\nFACTORIAL\n")

print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(5))
print(factorial(7))

print("\nNATURAL\n")

natural(1)
natural(0)
natural(5)
natural(7)
natural(13)

print("\nSUM OF DIGITS\n")

print(sum_of_digits(235))
print(sum_of_digits(731))
print(sum_of_digits(8261))
print(sum_of_digits(1914))
print(sum_of_digits(27522))

print("\nFIBONACCI\n")

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))

print("\nACKERMANN\n")

print(Ackermann(0,0))
print(Ackermann(0,1))
print(Ackermann(1,0))
print(Ackermann(1,1))
print(Ackermann(1,2))
print(Ackermann(2,1))
print(Ackermann(2,2))
print(Ackermann(2,3))
print(Ackermann(3,1))
print(Ackermann(3,2))
print(Ackermann(3,3))
print(Ackermann(3,4))
print(Ackermann(3,5))
print(Ackermann(3,6))
#print(Ackermann(3,7))
#print(Ackermann(3,8))
#print(Ackermann(3,9))
print(Ackermann(4,0))
#print(Ackermann(4,1))
#print(Ackermann(4,2))
#print(Ackermann(4,3))
#print(Ackermann(4,4))
#print(Ackermann(5,0))

print("\nLINEAR SEARCH\n")

def test_linear_search(lis, val):
    print(str(val) + " is in the list " + str(lis) + ": " + str(linear_search(lis, val)))

test_linear_search([4,5,1,6,3,56,7,2,4,2], 56)
test_linear_search([4,5,1,6,3,5,7,2,4,2], 56)

print("\nCOUNT INSTANCES\n")

def test_count_instances(lis, val):
    print(str(val) + " is in the list " + str(lis) + " " + str(count_instances(lis, val)) + " times.")

test_count_instances([4,5,1,6,3,56,7,2,4,2], 3)
test_count_instances([4,5,1,6,3,56,7,1,4,2], 2)
test_count_instances([4,5,1,6,3,5,7,2,4,2], 5)
test_count_instances([4,5,1,5,4,5,7,2,2,2], 4)
test_count_instances([4,5,1,5,4,5,7,2,2,2], 2)
test_count_instances([4,5,1,5,4,5,7,2,2,2], 5)
test_count_instances([7,7,7,7,7,7,7,7,7,7,7,7,7,7,7], 7)

print("\nARE DUPLICATES\n")

def test_duplicates(lis):
    print("There are duplicates in the list " + str(lis) + ": " + str(are_duplicates(lis)))

test_duplicates([4,5,1,6,3,56,7,2,4,2])
test_duplicates([9,5,1,6,3,0,7,8,4,2])
test_duplicates([9,5,1,6,3,0,7,2,4,2])

print("\nREMOVE DUPLICATES\n")

def test_remove_duplicates(lis):
    print("There list " + str(lis) + " without duplicates is " + str(remove_duplicates(lis)))

test_remove_duplicates([4,5,1,6,3,56,7,2,4,2])
test_remove_duplicates([9,5,1,6,3,0,7,8,4,2])
test_remove_duplicates([9,5,1,6,3,0,7,2,4,2])
test_remove_duplicates([4,5,1,5,4,5,7,2,2,2])
test_remove_duplicates([7,7,7,7,7,7,7,7,7,7,7,7,7,7,7])

print("\nSUBSTRING\n")

def test_substring(a_str, x):
    print("\nis " + x + " a substring in " + a_str + "?")
    print(is_substring(x, a_str))

test_substring("gagnaskipan", "") # EDGE CASE??

test_substring("gagnaskipan", "a")
test_substring("gagnaskipan", "gansk")
test_substring("gagnaskipan", "gnaski")
test_substring("gagnaskipan", "iganpsk")
test_substring("gagnaskipan", "gnAsk")
test_substring("gagnaskipan", "gnesk")
test_substring("gagnaskipan", "askipa")

print("\nX-ISH\n")

def test_x_ish(a_str, x):
    print("\nis " + a_str + " " + x + "-ish?")
    print(x_ish(a_str, x))

test_x_ish("gagnaskipan", "") # EDGE CASE??

test_x_ish("gagnaskipan", "a")
test_x_ish("gagnaskipan", "gnask")
test_x_ish("gagnaskipan", "iganpsk")
test_x_ish("gagnaskipan", "gnAsk")
test_x_ish("gagnaskipan", "gnesk")

print("\nPALINDROME\n")

def test_palindrome(a_str):
    if palindrome(a_str):
        print(str(a_str) + " is a palindrome")
    else:
        print(str(a_str) + " is NOT a palindrome")

test_palindrome("asdfdsa")
test_palindrome("asdffdsa")
test_palindrome("abda")
test_palindrome("adobe")
test_palindrome("adoba")