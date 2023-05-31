### EXERCISE 7 ###
"""
Using a for loop, output the values name, colour and price of each dictionary in the list
"""
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]

fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    name = fruit['name']
    colour = fruit['colour']
    price = fruit['price']
    print("Name:", name)
    print("Colour:", colour)
    print("Price:", price)
    print()  # Print an empty line after each fruit for separation