### EXERCISE 5 ###
"""
write a list comprehension expression to build a new list of EVEN numbers ONLY from range(5)

your sample output should be [0, 2, 4]
"""

# new_list = # your solution to be added here
new_list = [num for num in range(5) if num % 2 == 0]
print(new_list)

