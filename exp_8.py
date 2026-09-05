# 8. WAP to find the largest of three numbers

a = int(input("Enter first number: "))              # Input 1st number
b = int(input("Enter second number: "))             # Input 2nd number
c = int(input("Enter third number: "))              # Input 3rd number

if a > b and a > c:                                 # Check if a is the largest
    print("The largest number is:", a)
elif b > a and b > c:                               # Check if b is the largest
    print("The largest number is:", b)
else:                                               # Otherwise, c is the largest
    print("The largest number is:", c)