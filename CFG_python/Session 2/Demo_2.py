
name = "Luck"
def give_me (a_name):
    a_name = a_name + 'y'
    return a_name

print(give_me(name))


### EXERCISE 1 ###
"""
You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.
Write a program calculate how many pizzas you need to feed you and your friends.
Each friend will want half a pizza!
Use input() to grab your number of friends.
See if you can use int() to convert the output to a number!
Use print() to output your answer to console.
"""
# friends =
# pizza = 0.5
# print()

# Get the number of friends from the user
allMyFriends = int(input("How many friends?: "))

# Calculate the total number of pizzas needed (each friend wants half a pizza)
total_pizzas = (allMyFriends + 1) / 2  # Add 1 to include yourself

# Print the result
print("You need", total_pizzas, "pizzas to feed you and all your lovely friends.")

friends = input('How many friends are at your house? ')
pizzas = friends * 4
print("You need {} pizzas for {} friends".format(pizzas, friends))



### DEMO 1 ###
"""

Write a program that asks two questions using input()
then prints the values that were entered.
You can choose any questions that you want.

Example:
"""

animal = input('Do you like dogs or cats more? ')
pet_name = input('What would name your pet? ')
print(f'You like {} and you would name your pet {}'.format(animal, pet_name))



### DEMO 2 ###
"""
Show simple examples on how to use datetime package
"""

import datetime
x = datetime.datetime.now()
print(x)

########## formatting #############

import datetime
my_date = datetime.date(2022, 12, 31)
my_date.
print(my_date.strftime("%d/%b/%Y"))


### DEMO 3 ###
"""
Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) for £130.
If a person pays within 14 days, then the amount will be reduced to £65.

Pseudo-code Example:

- Accept the PCN date as an input
- Calculate the deadline date, which is 14 days from the PCT issue date.
- Print the message informing the driver about the deadline date, so that they only need to pay £65.

Example solution below.
"""

from datetime import datetime, timedelta

pcn_date = input("Please enter the PCN issue date in the following format DDMMYYYY: ")

date_obj = datetime.strptime(pcn_date, '%d%m%Y')

# Calculating the 14-day deadline

deadline = date_obj + timedelta(days=14)

# Formatting the date

formatted_deadline = deadline.date().strftime("%d %m %Y")

print("\n If you pay PCN penalty by *{}*, the amount will be reduced to £65".


import datetime

dt = datetime.datetime.now()
print(dt)  # check what we get back

# Format the timestamp
timestamp = dt.strftime("%Y%m%d_%H%M%S%f")[:-4]

print("timestamp: " + timestamp)


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

### EXERCISE 2 ###
# """
# fetch current date and time to milliseconds and create a "timestamp" in the following format YYYYMMDD_HHMMSSMsMs
#
# For example: if the current date and time is "30 October 2020, 10h 25 min 41 sec and 123456 milliseconds",
# out timestamp must be:

"20201030_22254112"

"""
# import datetime
#
# dt = datetime.datetime.now()
# print(dt)  # check what we get back
#
# timestamp = "your solution is here"
#
# print("timestamp: " + timestamp)


# ### EXERCISE 3 ####
# """
# # Write a very simple encoding program that accepts a word from a user and encodes it
# # by wrapping each letter with some other letters (symbols).
# #
# # Solution below - complete this together with the group
# """

# word = input("Enter the word you would like to encode: ")
#
# result = ''
#
# for char in word:
#     encoded = '{}'.format(char)
#     result = result + encoded
#
# print(result)

word = input("Enter the word you would like to encode: ")

result = ''

for char in word:
    encoded = '***{}***'.format(char)  # Modify the encoding pattern as desired
    result += encoded

print("Encoded word:", result)



### EXERCISE 1 ###
"""
You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.
Write a program calculate how many pizzas you need to feed you and your friends
"""

# friends = 6
# pizzas = friends * 0.5
#
# print('You need {} pizzas for {} friends'.format(pizzas, friends))

"""
Example solution with input
"""
# friends = int(input('How many friends are at your house? '))
# pizzas = friends * 0.5
# print('You need {} pizzas for {} friends'.format(pizzas, friends))






############################################################################################################
############################################################################################################
############################################################################################################



### EXERCISE 2 ###
"""
fetch current date and time to milliseconds and create a "timestamp" in the following format YYYYMMDD_HHMMSSMsMs

For example: if the current date and time is "30 October 2020, 10h 25 min 41 sec and 123456 milliseconds",
out timestamp must be:

"20201030_22254112"

"""

# import datetime
#
# dt = datetime.datetime.now()
# print(dt)  # check what we get back
#
# timestamp = dt.strftime('%Y%m%d_%H%M%S%f')[:-4]
#
# print("timestamp: " + timestamp)





############################################################################################################
############################################################################################################
############################################################################################################





### EXERCISE 3 ####
"""
Write a very simple encoding program that accepts a word from a user and encodes it
by wrapping each letter with some other letters (symbols).

Solution below - complete this together with the group
"""

word = input("Enter the word you would like to encode: ")

result = ''

for char in word:
    encoded = 'xyz{}abc'.format(char)
    result = result + encoded

print(result)

