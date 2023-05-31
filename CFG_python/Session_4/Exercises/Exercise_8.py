### EXERCISE 8 ###
"""
Write a program to create a random name.
You should have a list of random first-names and a list of last-names.
Choose a random item from each and display the result.

Extension: Using list of verbs and a list of nouns, create randomised sentences
"""
import random

first_names = ['John', 'Jane', 'Michael', 'Emily', 'William']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Taylor']

random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

random_name = random_first_name + ' ' + random_last_name

print("Random Name:", random_name)