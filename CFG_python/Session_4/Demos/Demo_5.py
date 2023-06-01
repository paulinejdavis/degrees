new_list = []

for word in ["cat", "dog", "rat", "cow"]:

    if word != "rat:":
        new_list.append(word)

print(new_list)

# new_list = [word for word in ['cat', 'dog','rat', 'cow'] if word != 'rat']
#
# print(new_list)

# same result - choose preference