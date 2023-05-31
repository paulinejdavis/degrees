
### EXERCISE 5 ###
"""
This program uses random to simulate a coin flip.

To finish the program you will need to add the following:

If the random coin flip matches the choice input by the user then they win
Otherwise if the random coin flip does not match the choice input by the user then they lose
"""

# import random
#
# def flip_coin():
#     # your code goes here
#
# choice = input('heads or tails: ')
# result = flip_coin()
#
# print('The coin landed on {}'.format(result))


################################################
###           PALINDROME EXERCISE            ###
################################################

def isPalindrome(string):
    # Compare characters using a single pointer starting from both ends of the string
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


print(isPalindrome('hannah'))  # should return True
print(isPalindrome('mummy'))  # should return False
print(isPalindrome('I'))  # should return True


# def isPalindrome(s):
#     return s == s[::-1]
#
# s = "hannah"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")