# 6. WAP to demonstrate working with tuples in Python.
tup = (10, 20, 40, 30, 50, 30, 60, 30)                  # creating a tuple
print("Original tuple:", tup)
print("Length of original tuple:", len(tup))            # length of the tuple
print("Maximum value in original tuple:", max(tup))     # Max value in the tuple
print("Minimum value in original tuple:", min(tup))     # Min value in the tuple
print("Sum of the elements in the tuple:", sum(tup))    # Sum of the elements in the tuple
print("Count of 30 in the tuple:", tup.count(30))       # Count of 30 in the tuple
print("Index of 40 in the tuple:", tup.index(40))       # Index of 40 in the tuple
print("25 is not present:", 25 not in tup)              # Membership operator
print("First element: ", tup[0])                        # Accessing first element
print("Last element: ", tup[-1])                        # Accessing last element
print("First five elements: ", tup[:5])                 # Accessing first five elements
print("Elements from index 2 to 5: ", tup[2:6])         # Accessing elements from index 2 to 5
print("Reversed tuple: ", tup[::-1])                    # Reversing the tuple

tup2 = (70, 80, 90)
tup3 = tup + tup2
print("Concatenated tuple: ", tup3)                     # Concatenating tuples
repeated_tup = tup * 2
print("Repeated tuple: ", repeated_tup)                 # Repeating the tuple
print("Reversed Tuple", tuple(reversed(tup)))           # Reversing the tuple using reversed function
print("Sorted Tuple", tuple(sorted(tup)))               # Sorting the tuple using sorted function
print("All elements are non-zero?", all(tup))           # Check if all elements are non-zero
print("Any element is non-zero?", any(tup))             # Check if any element is non-zero
copy_tup = tup[:]                                       # Copying the tuple 
print("Copied Tuple: ", copy_tup)
print("Type of the tuple: ", type(tup))                 # Type of the tuple
