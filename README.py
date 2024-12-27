import random
import time

def fib(n):

    if n <= 0:
        return "Fibonacci number must be a positive integer!"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

def fibonacci_magic(n):
    
    random.seed(time.time())  
    chars = ['@', '#', '&', '%', '$', '*', '!', '^', '?', '(', ')']  
    random.shuffle(chars)  

    
    fib_sequence = fib(n)
    scrambled_sequence = [str(fib_sequence[i]) + random.choice(chars) for i in range(len(fib_sequence))]


    print("Scrambled Fibonacci Sequence:")
    print(" ".join(scrambled_sequence))

    time.sleep(2)  
    print("\nSurprise!")
    time.sleep(1)
    print("Only one number remains from the Fibonacci sequence: 5")
    return [5]


n = int(input("Enter the number of Fibonacci sequence elements (e.g., 10): "))
result = fibonacci_magic(n)


print("\nFinal Result: ", result)
