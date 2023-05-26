### DEMO 1 ###
"""

Write a program that asks two questions using input()
then prints the values that were entered.
You can choose any questions that you want.

Example:
"""

animal = input('Do you like dogs or cats more? ')
pet_name = input('What would name your pet? ')
print('You like {} and you would name your pet {}'.format(animal, pet_name))

"""
The input() always returns a string value!!! 
You can convert this string value to an integer with int():

Demonstrate this case with the following examples:
--------------------------------------------------

apples_string = '12'
total_apples = int(apples_string) + 5
print(total_apples) 

AND

purchased_apples = input('How many apples did you buy? ')
total_apples = int(purchased_apples) + 5
print(total_apples)

"""