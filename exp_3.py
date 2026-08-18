# Write a program to create, concatenate and print a string 
# and accessing sub-string from a given string.
        # Sting Creation
str1 = input("Enter the first string: ")    # Taking input for the first string
str2 = input("Enter the second string: ")   # Taking input for the second string

print(f"The first string is: {str1}")   # Printing the first string
print(f"The second string is: {str2}")  # Printing the second string

        # String Concatenation
str3 = str1 + " " + str2   # Concatenating the two strings with a space in between
print(f"The concatenated string is: {str3}")  # Printing the concatenated string

        # Accessing Sub-string
sub_str = str3[0:6]   # Accessing the first 6 characters of the concatenated string
print(f"The sub-string from the concatenated string is: {sub_str}")  # Printing the sub-string


# Output:
# Enter the first string: DAVIET
# Enter the second string: Jalandhar
# The first string is: DAVIET
# The second string is: Jalandhar
# The concatenated string is: DAVIET Jalandhar
# The sub-string from the concatenated string is: DAVIET


# Submitted by: 
# Dhruv Narula
# B.Tech CSE (AI & ML) 5th-A
# Class Roll No: 434/24
# University Roll No: 2427958