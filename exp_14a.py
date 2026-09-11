''' 14. WAP to define a module to find Fibonacci numbers and import the module to another program.'''

# Module File: exp_14a.py
def fibonacci(n):    # Function to generate Fibonacci numbers up to n
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence