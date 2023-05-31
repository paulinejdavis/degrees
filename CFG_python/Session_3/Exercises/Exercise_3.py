### EXERCISE 3 ###

"""
Rewrite the output of your burger program to use if statements

If it is a good choice it should be:

    "This restaurant is a great choice!"

If it is not a good choice it should be:

    "Probably not a good idea"

"""

price = float(input("Enter the price of the burger: "))
vegetarian_option = input("Does the restaurant have a vegetarian option? (y/n): ").lower() == 'y'
within_budget = price <= 10.00

if within_budget and vegetarian_option:
    print("This restaurant is a great choice!")
else:
    print("Probably not a good idea")
