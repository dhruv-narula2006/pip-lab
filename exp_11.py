# 11. Write a Python script that prints prime numbers less than 20.

def isPrime(n):           # Function for determining whether a number is prime or not
    if n <=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Main Execution
print("Prime Numbers Less than 20 are:")
for x in range(2, 20):
    if isPrime(x):
        print(x, end = " ")