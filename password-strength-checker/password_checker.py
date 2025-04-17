import re

def check_password_strength(password):
    # Define rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is None

    # Dictionary of failed checks
    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing digit": digit_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing special symbol": symbol_error
    }

    # Gather failed checks
    failed = [msg for msg, error in errors.items() if error]

    # Classify strength
    if not failed:
        return "✅ Strong password!"
    elif len(failed) <= 2:
        return f"⚠️ Moderate password. Consider fixing: {', '.join(failed)}"
    else:
        return f"❌ Weak password. Issues: {', '.join(failed)}"

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    user_input = input("Enter your password: ")
    result = check_password_strength(user_input)
    print("\n" + result)

