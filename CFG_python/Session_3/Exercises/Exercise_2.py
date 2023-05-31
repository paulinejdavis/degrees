
### EXERCISE 2 ###

"""
Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget AND has a vegetarian option

    Restaurant meets criteria: True

"""

price = float(input("Enter the price of the burger: "))
vegetarian_option = input("Does the restaurant have a vegetarian option? (y/n): ").lower() == 'y'
within_budget = price <= 10.00
meets_criteria = within_budget and vegetarian_option
print("Restaurant meets criteria:", meets_criteria)
