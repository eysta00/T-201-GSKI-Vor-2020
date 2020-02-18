from time import time

def fibonacci_slow(n): 
    if n<0: 
        print("Incorrect input")  
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci_slow(n-1)+fibonacci_slow(n-2)

def fibonacci_fast(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

start_time = time()
#fib = fibonacci_slow(35) 
# fibonacchi slow can barely manage 40 while fibonacci fast can go much more
# the reason this happens is because instance of recursions happens 2^x while
# fib fast uses a for loop instead.
fib = fibonacci_fast(90000)
end_time = time()
elapsed = end_time - start_time

def main():
    print("Fib timer using two diffrent methods of calculation a fib number")
    print("\n\tChoose a method\n\n\
        1. for loop method\n\n\
        2. recursion method\n\n\
        \tinput anything else to quit")
    try:
        user_input = int(input("Input a method you want to test: "))
        while user_input == 1 or user_input == 2:
            
            user_num = int(input("Input a number you want calculated: "))
            if user_input == 1:
                start_time = time()
                fib_1 = fibonacci_fast(user_num)
                end_time = time()
                elapsed = end_time - start_time
                str_1 = "{:.2f} seconds".format(elapsed)
                print(str_1)
                user_input = int(input("\nInput a method you want to test or anything else to quit: "))

            elif user_input == 2:
                start_time = time()
                fib_2 = fibonacci_slow(user_num)
                end_time = time()
                elapsed = end_time - start_time
                instances = 2 ** user_num
                str_2 = "{:.2f} seconds, instances created = {:,}".format(elapsed, instances)
                print(str_2)
                user_input = int(input("\nInput a method you want to test or anything else to quit: "))
    
    except ValueError:
        print("invalid input")

main()