### EXERCISE 1 ###
"""
Create a to-do list program that writes user input to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items

NB: You will need to manually create a new file called todo.txt in the same folder as your program before you start.
"""
user_input = input("Here's your to-do list: ")

file_path = "/Users/paulinejdavis/Documents/degrees/CFG_python/Session_5/Exercises/todo.txt"

# Write the user input to the file
with open(file_path, 'w') as file:
    file.write(user_input)

# Read and print the contents of the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)