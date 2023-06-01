import random

first_names = ["Jim", "Buddy", "Wolf", "River"]
last_names = ["Love", "Bronx", "Money", "Kerr"]

random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

random_name = random_first_name + " " + random_last_name
print(random_name)