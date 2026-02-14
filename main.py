# ==========================================
# Python Utility Toolkit - PRO Version
# ==========================================


# ---------------------------
# Utility Input Functions
# ---------------------------

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid number. Please try again.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid integer. Please enter a valid whole number.")


# ---------------------------
# Login System
# ---------------------------

def login_system():
    USERNAME = "admin"
    PASSWORD = "1234"

    attempts = 3

    print("\n=== Login Required ===")

    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == USERNAME and password == PASSWORD:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")

    print("Too many failed attempts. Exiting program.")
    return False


# ---------------------------
# Calculator with History
# ---------------------------

calculation_history = []


def advanced_calculator():
    print("\n--- Advanced Calculator ---")

    num1 = get_float_input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    num2 = get_float_input("Enter second number: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator selected.")
        return

    calculation = f"{num1} {operator} {num2} = {result}"
    calculation_history.append(calculation)

    print("Result:", result)


def view_history():
    print("\n--- Calculation History ---")
    if not calculation_history:
        print("No calculations yet.")
        return

    for index, record in enumerate(calculation_history, start=1):
        print(f"{index}. {record}")


def clear_history():
    calculation_history.clear()
    print("History cleared successfully.")


# ---------------------------
# Password Strength Analyzer
# ---------------------------

def password_strength_analyzer():
    print("\n--- Password Strength Analyzer ---")

    password = input("Enter password: ")

    if password == "":
        print("Password cannot be empty.")
        return

    length_score = len(password) >= 8
    upper_score = any(c.isupper() for c in password)
    lower_score = any(c.islower() for c in password)
    digit_score = any(c.isdigit() for c in password)
    special_score = any(not c.isalnum() for c in password)

    score = sum([length_score, upper_score, lower_score, digit_score, special_score])

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("Password Strength:", strength)


# ---------------------------
# Number Analyzer
# ---------------------------

def number_analyzer():
    print("\n--- Number Analyzer ---")

    number = get_int_input("Enter an integer: ")

    if number == 0:
        sign = "Zero"
    elif number > 0:
        sign = "Positive"
    else:
        sign = "Negative"

    parity = "Even" if number % 2 == 0 else "Odd"

    print("Number Type:", sign)
    print("Parity:", parity)


# ---------------------------
# Text Analyzer
# ---------------------------

def text_analyzer():
    print("\n--- Text Analyzer ---")

    text = input("Enter text: ")

    if text.strip() == "":
        print("Text cannot be empty.")
        return

    word_count = len(text.split())
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print("Word Count:", word_count)
    print("Character Count:", char_count)
    print("Sentence Count:", sentence_count)


# ---------------------------
# Main Menu
# ---------------------------

def display_menu():
    print("\n=================================")
    print(" Python Utility Toolkit - PRO")
    print("=================================")
    print("1. Advanced Calculator")
    print("2. View Calculator History")
    print("3. Clear Calculator History")
    print("4. Password Strength Analyzer")
    print("5. Number Analyzer")
    print("6. Text Analyzer")
    print("7. Exit")


def main():
    if not login_system():
        return

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            advanced_calculator()
        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            password_strength_analyzer()
        elif choice == "5":
            number_analyzer()
        elif choice == "6":
            text_analyzer()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 7.")


# Entry Point
if __name__ == "__main__":
    main()
