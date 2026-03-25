num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Select the operation you want to perform (+, -, *, /):")
if operation == "+":
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)
elif operation == "-":
    result = num1 - num2
    print("The difference of", num1, "and", num2, "is", result)
elif operation == "*":
    result = num1 * num2
    print("The product of", num1, "and", num2, "is", result)
elif operation == "/":
    result = num1 / num2
    print("The quotient of", num1, "and", num2, "is", result)
else:
    print("Invalid operation selected.")