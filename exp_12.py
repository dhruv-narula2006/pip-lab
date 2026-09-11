# 12. WAP to find the factorial of a number using recursion.

def factorial(n):          # Function to find factorial
    if n ==0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)  # Recursive call to the function factorial()

# Main Execution
x = int(input("Enter the number whose factorial you want: "))
print(f"Factorial of {x}: ", factorial(x))