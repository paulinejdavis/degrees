### DEMO 5 ###
"""
Due to social distancing, only 10 people are allowed to be inside a shop at the same time.
This program invites people in the queue to come in while we have some capacity.
"""

store_capacity = 10  # people

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1

print("\nPlease wait for someone to exit the store.")