# 5. WAP to create, append, and remove lists in python.
nums = [20, 35, 45, 35, 20, 10, 20]                   # creating a list
print("Original list:", nums)
print("Length of original list:", len(nums))          # finding the length of the list 
print("Maximum value in original list:", max(nums))   # finding the maximum value in the list
print("Minimum value in original list:", min(nums))   # finding the minimum value in the list
print("Sum of the elements in the list:", sum(nums))  # finding the sum of all elements in the list
print("Count of 20 in the list:", nums.count(20))     # counting the occurrences of 20 in the list
print("Index of 35 in the list:", nums.index(35))     # finding the index of the first occurrence of 35

print("\n Adding elements to the original list....")
nums.append(50)                                       # appending an element at the end of the list
print("List after appending: ", nums)
nums.insert(2, 25)                                    # inserting an element at index 2
print("List after inserting 25 at index 2: ", nums)

print("\n Removing elements from the list....")
nums.remove(35)                                      # removing the first occurrence of 35
print("List after removing 35: ", nums)
nums.pop()                                           # removing the last element
print("List after popping the last element: ", nums)

print("\n Sorting the list....")
nums.sort()                                         # sorting the list in ascending order
print("List after sorting: ", nums)
nums.sort(reverse=True)                             # sorting the list in descending order
print("List after sorting in descending order: ", nums)
nums.reverse()                                      # reversing the list
print("List after reversing: ", nums)

print("\n Copying, reversing and sorting the list....")
nums_copy = nums.copy()                             # creating a copy of the list
print("Copied list: ", nums_copy)
print("Reversed function: ", list(reversed(nums)))  # using reversed function to reverse the list
print("Sorted function: ", sorted(nums))            # using sorted function to sort the list

print("\n Another functions....")
print("Is 25 in the list? ", 25 in nums)            # Membership operator
a = any(nums)                                   # checking if any element is non-zero
print("Is any element non-zero in the list? ", a)
b = all(nums)                                   # checking if all elements are non-zero
print("Are all elements non-zero in the list? ", b)

print("\n Clearing the list....")
nums.clear()                                    # clearing all elements from the list
print("List after clearing: ", nums)