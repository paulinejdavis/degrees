### DEMO 5 ###
"""
Review our solution for a previous exercise, namely

line = line.translate(line.maketrans("", "", string.punctuation))
"""

# import string
#
# """
# Let's build a translator
# 1. This uses the 3-argument version of str.maketrans
# 2. There are 3 arguments (x, y, z) where 'x' and 'y'must be equal-length strings and characters in 'x' are replaced by characters in 'y'.
# 3. 'z' is a string (string.punctuation here) where each character in the string is mapped to None
#
# """
# translator = str.maketrans('', '', string.punctuation)
#
# """
# This is an alternative that creates a dictionary mapping of every character from string.punctuation to None
# (this will also work)
#
# translator = str.maketrans(dict.fromkeys(string.punctuation))
# """
#
#
# s = 'This#! is a string, with-- all (sorts) of punctuation& that needs to be!!! cleaned up?'
#
# # pass the translator to the string's translate method.
# print(s.translate(translator))