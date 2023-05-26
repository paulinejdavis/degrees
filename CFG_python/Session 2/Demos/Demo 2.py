### DEMO 2 ###
"""
Show simple examples on how to use datetime package
"""

import datetime
x = datetime.datetime.now()
print(x)

########## formatting #############

import datetime
my_date = datetime.date(2022, 12, 31)
print(my_date.strftime("%d/%b/%Y"))