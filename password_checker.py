# Password Strength Checker
import re

def pass_check(password):
    score = 0
    if len(password) >= 6:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[!@#$%^&*()_+]', password):
        score += 1

    if score == 5:
        return "Strong Password"
    elif score == 4:
        return "Medium Password"
    elif score == 3:
        return "Weak Password"
    else:
        return "Invalid Password"

password = input("Enter a password: ")
result = pass_check(password)
print(result)
