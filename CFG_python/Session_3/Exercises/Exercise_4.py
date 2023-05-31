### Exercise 4 ###

"""
1 Else exercise:

Now that you've finished your burger, you want to pay for your food.
Let's write a program to calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%.
The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.
"""

meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

if meal_price > 20 and discount_applicable:
    discounted_price = meal_price * 0.9
    print("Discount applied")
    print("Total cost after discount: £", discounted_price)
else:
    print("No discount")
    print("Total cost: £", meal_price)



"""
2 Elif Exercise:

You're cooking a pizza and need to check that the oven is at the right temperature.

Write a program to:

Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature
"""

temperature = float(input('What is the temperature of the oven? '))

if temperature > 200:
    print("The oven is too hot")
elif temperature < 150:
    print("The oven is too cold")
elif temperature == 180:
    print("The oven is at the perfect temperature")
else:
    print("The temperature is close enough")
