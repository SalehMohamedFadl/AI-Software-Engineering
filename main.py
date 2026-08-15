"""
Advanced Greeting App
A more feature-rich version of a simple "Hello, name" script.
"""

import re
import datetime


def get_time_based_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        if not re.fullmatch(r"[A-Za-z '-]+", name):
            print("Please use only letters, spaces, hyphens, or apostrophes.")
            continue
        return name.title()


def get_valid_age():
    while True:
        age_input = input("Enter your age (or press Enter to skip): ").strip()
        if age_input == "":
            return None
        if age_input.isdigit() and 0 < int(age_input) < 130:
            return int(age_input)
        print("Please enter a valid age between 1 and 129.")


def build_welcome_message(name, age):
    greeting = get_time_based_greeting()
    message = f"{greeting}, {name}! Welcome to AI Software Engineering."
    if age is not None:
        years_to_100 = 100 - age
        if years_to_100 > 0:
            message += f" You have {years_to_100} year(s) to go until you turn 100!"
        elif years_to_100 == 0:
            message += " You're turning 100 this year! 🎉"
        else:
            message += " You've already passed the century mark. Impressive!"
    return message


def print_banner():
    banner = r"""
     _    ___    ____             _____
    / \  |_ _|  / ___|_      __  | ____|_ __   __ _
   / _ \  | |   \___ \ \ /\ / /  |  _| | '_ \ / _` |
  / ___ \ | |    ___) \ V  V /   | |___| | | | (_| |
 /_/   \_\___|  |____/ \_/\_/    |_____|_| |_|\__, |
                                               |___/
    """
    print(banner)


def main():
    print_banner()
    name = get_valid_name()
    age = get_valid_age()
    message = build_welcome_message(name, age)
    print("\n" + "-" * len(message))
    print(message)
    print("-" * len(message))


if __name__ == "__main__":
    main()