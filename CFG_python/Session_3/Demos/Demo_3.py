# requesting user for temperature
temperature = input("What is the temperature?")

is_freezing = float(temperature) <= 0.0

print("The temperature is freezing: {}".format(is_freezing))