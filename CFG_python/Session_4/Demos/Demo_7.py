#tuples - can't change elements in a tuple. it's immutable
#tyuples behave list lists

order = ('croissant', 'coffee', 'orange juice')
result = set(order)
print(result)
#
# order.append('porridge')
# ☝🏽 throws an error

# print(order)

# set is unordered and unindexed - unique displays in a random order

my_set = {1,2,3}
my_set.add(4)
# my_set.append(3) #doesnt work
print(my_set)