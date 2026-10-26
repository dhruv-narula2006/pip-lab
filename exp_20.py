# 20. Write a Python class to reverse a string word by word.
class WordReverser:
    def __init__(self, string):
        self.string = string
    def reverse_words(self):
        words = self.string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage:
try:
    input_string = input("Enter a string: ")
    reverser = WordReverser(input_string)
    reversed_string = reverser.reverse_words()
    print(f"The reversed string is: {reversed_string}")
except Exception as e:
    print(f"An error occurred: {e}")