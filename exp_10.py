# 10. WAP to print the following pattern using nested for loop.

n = int(input("Enter the number of rows: "))        # Input the no. of rows
for i in range(0, n):                               # Increasing rows
    for j in range(i+1):
        print("*", end=" ")                         # Print star
    print()                                         # Move to the next line

for i in range(n-1, 0, -1):                         # Decreasing rows
    for j in range(i):
        print("*", end=" ")                         # Print star
    print()                                         # Move to the next line