### DEMO 8 ###
"""
Positional Arguments

Positional arguments values are copied to their corresponding parameters in order.
You must to pass arguments in the order in which they are defined.
"""

# # Correct arguments order
# def some_function(name, job):
#     print(name, 'is a', job)
#
#
# some_function('Fiona', 'developer')

# ---------------------------------------


# # Wrong arguments order
# def some_function(name, job):
#     print(name, 'is a', job)
#
#
# some_function('developer', 'Fiona')

"""
Keyword Arguments

you can pass arguments using the names of their corresponding parameters.
in this case, the order of the arguments no longer matters.
you can combine positional and keyword arguments in a single call.
if you do so, specify the positional arguments before keyword arguments.
"""

# def some_function(name, job):
#     print(name, 'is a', job)
#
#
# some_function(job='developer', name='Fiona')
#
# some_function(name='Fiona', job='developer')


"""
Default Arguments¶
You can specify default values for arguments when defining a function.
The default value is used IF the function is called without a corresponding argument.
"""

# def some_function(name, job='developer'):
#     print(name, 'is a', job)
#
#
# some_function('Fiona')
#
# some_function('Fiona', 'manager')

"""
Variable Length Arguments (*args and **kwargs)¶
Variable length arguments are useful when you want to create functions that take unlimited number of arguments.
Unlimited in the sense that you do not know beforehand how many arguments can be passed to your function by the user.

*args¶
When you prefix a parameter with an asterisk *, it collects all the unmatched positional arguments into a tuple
(we will learn about tuples later, think of it as a collection of items aka a box with numbers or words etc) .


**kwargs
The ** syntax is similar, but it only works for keyword arguments (aka corresponding pairs)
"""

# def print_arguments(*args):
#     print(args)
#
#
# print_arguments(1, 2, 3, 4, 5, 6, 7)

# ----------------------------------


# def print_arguments(**kwargs):
#     print(kwargs)
#
#
# print_arguments(name='Fiona', age=25, job='developer')