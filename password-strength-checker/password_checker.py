import re

def password_checker(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

password = input("Enter your password: ")

if password_checker(password):
    print("Password is strong.")
else:
    print("Password is weak.")

