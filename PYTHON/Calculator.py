print("====================================")
print("| Welcome to the Calculator Program |")
print("====================================")

print("Select operation you want to perform:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = input("Enter choice(1/2/3/4): ")
print("You have selected:", choice)
num1 = float(input(f"Enter the first number: "))
num2 = float(input(f"Enter the second number: "))

results = []
if choice == '1':
    result = num1 + num2
    results.append(result)
elif choice == '2':
    result = num1 - num2
    results.append(result)
elif choice == '3':
    result = num1 * num2
    results.append(result)
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero")
        results.append("Error")
    else:
        result = num1 / num2
        results.append(result)
else:
    print("Invalid input")

print(f"Result : {results}")
print("Thank you for using the calculator")
