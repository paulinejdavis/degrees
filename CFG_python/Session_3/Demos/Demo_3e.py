import random

sides = int(input("How many sides does the die have? "))
random_integer = random.randint(1, sides)

print("you rolled a {}".format(random_integer))