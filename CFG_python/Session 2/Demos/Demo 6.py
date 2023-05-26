### DEMO 6 ###
"""
Example INFINITE 'while loop' that runs forever until the memory is 'blown'
"""

store_capacity = 10

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    # store_capacity =  store_capacity - 1 ---> imagine that we forgot to add this logic!!!

print("\nPlease wait for someone to exit the store.")
