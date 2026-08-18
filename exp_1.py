# 1. Write a program to demonstrate different number datatypes in python.

a  = 125                                        # integer datatype
print(f"The value of a is {a}")
print(f"The type of a is {type(a)}")            # Printing the datatype of a

b = 12.256                                   # float datatype
print(f"The value of b is {b}")
print(f"The type of b is {type(b)}")            # Printing the datatype of b

c = 12 + 5j                                    # complex datatype
print(f"The value of c is {c}")
print(f"The type of c is {type(c)}")            # Printing the datatype of c

d = 5 < 12                                     # boolean datatype
print(f"The value of d is {d}")
print(f"The type of d is {type(d)}")           # Printing the datatype of d

e = float(a)                                    # converting integer to float
print(f"The converted value of a is {e}")
print(f"The new type of a is {type(e)}")        # Printing the new datatype of a

f = int(b)                                      # converting float to integer
print(f"The converted value of b is {f}")
print(f"The new type of b is {type(f)}")        # Printing the new datatype of b

g = int(d)                                      # converting boolean to integer
print(f"The converted value of d is {g}")
print(f"The new type of d is {type(g)}")        # Printing the new datatype of d


# Output:
# The value of a is 125
# The type of a is <class 'int'>
# The value of b is 12.256
# The type of b is <class 'float'>
# The value of c is (12+5j)
# The type of c is <class 'complex'>
# The value of d is True
# The type of d is <class 'bool'>
# The converted value of a is 125.0
# The new type of a is <class 'float'>
# The converted value of b is 12
# The new type of b is <class 'int'>
# The converted value of d is 1
# The new type of d is <class 'int'>


# Submitted by: 
# Dhruv Narula
# B.Tech CSE (AI & ML) 5th-A
# Class Roll No: 434/24
# University Roll No: 2427958