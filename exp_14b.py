# Program File: exp_14b.py
import exp_14a as fib_module

n = int(input("Enter the number of terms to generate Fibonacci sequence : "))
fibonacci_sequence = fib_module.fibonacci(n)  # Calling the function from the module
print(f"Fibonacci sequence up to {n}: ")
for i in fibonacci_sequence:
    print(i, end=' ')