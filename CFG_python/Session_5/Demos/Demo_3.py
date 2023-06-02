### DEMO 3 ###
"""
Demonstrate how to write to a file

# CHNAGE the path to the location where your file will be saved
# Note that you may need to change '\' to '\\' to espace symbols

"""

file = open('C:\\path-to-the-file-location\\NEW-FILE-NAME.txt', 'w')

file.write("Frankly, my dear, I don't give a damn. (GONE WITH THE WIND)")
file.close()


"""
Let's ADD more lines to the file
note the new line '\n'

CHANGE the path to the location where your file will be saved
"""

movie_quotes = [
    "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ)",
]

file = open('C:\\path-to-the-file-location\\NEW-FILE-NAME.txt', 'a')  # NB 'a' mode for append

file.writelines(movie_quotes)
file.close()
