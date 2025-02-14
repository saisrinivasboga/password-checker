import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one uppercase letter.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one lowercase letter.\n"

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "Password should contain at least one digit.\n"

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one special character (@, $, !, %, *, ?, &).\n"

    # Provide feedback
    if strength == 5:
        return "Strong Password ✅"
    elif strength >= 3:
        return "Moderate Password ⚠\n" + remarks
    else:
        return "Weak Password ❌\n" + remarks

# Get user input
password = input("Enter your password: ")
result = check_password_strength(password)
print("\n" + result)
