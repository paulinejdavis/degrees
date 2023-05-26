### DEMO 4 ###
"""
The pre-written range() function can be used to make a for loop repeat a certain number of times.

The range() function starts counting from 0

Examples below
"""
for number in range(5):
    print(number)


for number in range(5):
    print("executing a block of code within FOR LOOP - run No {}".format(number))
    # replace (number) with (number + 1)


total = 0
for number in range(3):  # remember --> 0, 1, 2

    print("total value is: " + str(total))
    print("this is run No " + str(number) + " inside the loop \n")
    total = total + 10

print("\nWe are outside the loop now")
print("the final value is: " + str(total))