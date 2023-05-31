mars_choice = input("Would you like to visit Mars? y/n")
is_willing = mars_choice == 'y'

affordable = input("Can you afford to visit mars? y/n")
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print("You should visit mars:{}".format(should_visit_mars))