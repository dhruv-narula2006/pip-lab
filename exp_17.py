'''17. Write a Python program that inputs a text file. This program should print all the unique words in the file in alphabetical order.'''

import re
infile = input("Enter the name of the text file: ")
try:
    with open(infile, 'r') as file:
        text = file.read()
        text_lowercase = text.lower()  # Convert text to lowercase
        cleaned_text = re.sub(r'[^a-z0-9\s]', '', text_lowercase)  # Removing Special characters
        words = cleaned_text.split()  # Split the text into words
        unique_words = sorted(set(words))  # Get unique words and sort them alphabetically
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
            
except FileNotFoundError:
    print(f"The file '{infile}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")