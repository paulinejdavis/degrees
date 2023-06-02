### DEMO 4 ###
"""
Writing and reading files using CSV library in Python.
"""
# Write and Read ('w+'): This mode opens the file for both reading and writing.
# Writing a csv

import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# ======================================
# Reading a CSV

# import csv
#
# with open('team.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     for row in spreadsheet:
#         print(dict(row))

# file = open('/Users/paulinejdavis/Documents/degrees/CFG_python/Session_5/Demos/team.csv', 'r')
#
# content = file.read()
# print(content)
#
# with open('people.txt', 'w+') as text_file:
#     people = 'Jim, \nJoe, \nScooby,'
#     text_file.write(people)
