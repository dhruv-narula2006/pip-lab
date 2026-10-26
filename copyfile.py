'''16. Write a Python script named copyfile.py. This script should prompt the user for names of two text files. The contents of first file should be input and written into the second file.'''
file1 = input("Enter the name of the first text file: ")
file2 = input("Enter the name of the second text file: ")

try:
    with open(file1, 'r') as source_file:
        content = source_file.read()

    with open(file2, 'w') as destination_file:
        destination_file.write(content)

    print(f"Contents of '{file1}' have been copied to '{file2}'.")

except FileNotFoundError:
    print(f"Error: The file '{file1}' does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")