### DEMO 1 ###
"""
Demonstrate how to read file contents.

CHANGE the path to the location where your file called 'text_fle.txt' is saved
Note that you may need to change '\' to '\\' to espace symbols

Here is an example: file = open('C:\\Users\\olyan\\Desktop\\test_file.txt', 'r')

"""
file = open('C:\\path-to-the-file-location\\test_file.txt', 'r')

print(file) # What do we get?

"""
The file object returned by open() function is an object of type _io.TextIOWrapper. 

We need to use special methods to read/write data from/to this object. 
Let's go back to the slide deck to see how it is done.  
"""

