name = input("What is your name? ")
is_admin = name == "admin"

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print("welcome")

if not is_admin or not is_password_correct:
    print("go away")