"""
Simple Calculator
Supports: addition, subtraction, multiplication, division
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operator():
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operator. Please choose one of +, -, *, /.")


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)


def main():
    print("=== Simple Calculator ===")
    while True:
        num1 = get_number("Enter first number: ")
        op = get_operator()
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(num1, op, num2)
            print(f"Result: {num1} {op} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()