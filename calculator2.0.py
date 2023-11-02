print("====================================")
print("| Welcome to the Calculator Program |")
print("====================================")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def calculator():
    print("Select operation you want to perform:")
    print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    print("You have selected:", choice)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)
    else:
        print("Invalid input")
        return

    print("Thank you for using the calculator")

calculator()
