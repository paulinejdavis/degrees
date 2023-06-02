### EXERCISE 3 ###
"""
PROBLEM SOLVING WITH PYTHON --> 

Write a Python program to count the occurrences of a word in a text file.
Your program will take a word from the user and count the number of occurrences of that word in a file.

(use file: 5.3_example_one.txt, save this file in the same folder as your Python program! )
"""

def count_word_occurrences(file_path, word):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            occurrences = content.count(word.lower())
            return occurrences
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Prompt the user for the word to count occurrences
word = input("Enter the word to count occurrences: ")

# Specify the file path
file_path = "/Users/paulinejdavis/Documents/degrees/CFG_python/Session_5/Exercises/5.3_example_one.txt"

# Call the function to count occurrences
count = count_word_occurrences(file_path, word)

# Print the result
print(f"The word '{word}' occurs {count} time(s) in the file.")
