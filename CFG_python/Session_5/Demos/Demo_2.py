### DEMO 2 ###
"""
Objective is to demonstrate how to read content(s) from a file object.

CHANGE the path to the location where your file called 'text_fle.txt' is saved
Note that you may need to change '\' to '\\' to espace symbols
Here is an example: file = open('C:\\Users\\olyan\\Desktop\\test_file.txt', 'r')
"""

file = open('C:\\path-to-the-file-location\\test_file.txt', 'r')

"""
Read() example
"""
content = file.read()  # NB: try passing a number as an arg. like read(3)
print(content)


"""
Readline() example
"""
# content = file.readline()
# print(content)


"""
Readline() example
"""
# content = file.readlines()
# print(content)

# alternatively try pretty print to see each file row on a new line
# uncomment this

# print('')
# from pprint import pprint as pp
# pp(content)


"""
IMPORTANT: now that we have finished our operations with the file, we must CLOSE it. 
Otherwise it would still be open and changes not save. 
Also others cannot access the file while it is open.
"""

# we need to run this

# file.close()

