
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#operation = input("Select the operation you want to perform (+, -, *, /):")
#if operation == "+":
#    result = num1 + num2
#    print("The sum of", num1, "and", num2, "is", result)
#elif operation == "-":
#    result = num1 - num2
#    print("The difference of", num1, "and", num2, "is", result)
#elif operation == "*":
#    result = num1 * num2
#    print("The product of", num1, "and", num2, "is", result)
#elif operation == "/":
#    result = num1 / num2
#    print("The quotient of", num1, "and", num2, "is", result)
#else:
#    print("Invalid operation selected.")

string = input()
def calculator(string):
    operations = []
    for i in string:
        if i =="/":
            operations.append("/")
        elif i=="*":
            operations.append("*")
        elif i=="+":
            operations.append("+")
        elif i=="-":
            operations.append("-")
    numbers = []
    str1 = string
    for i in range(len(operations)):
        str1 = str1.split(operations[i], 1)
        numbers.append(float(str1[0].strip()))
        str1 = str1[1].strip()
    numbers.append(float(str1[0].strip()))
    while len(operations) > 0:
        if "/" in operations:
            index = operations.index("/")
            result = numbers[index] / numbers[index + 1]
            numbers[index] = result
            numbers.pop(index + 1)
            operations.pop(index)
        elif "*" in operations:
            index = operations.index("*")
            result = numbers[index] * numbers[index + 1]
            numbers[index] = result
            numbers.pop(index + 1)
            operations.pop(index)
        elif "+" in operations:
            index = operations.index("+")
            result = numbers[index] + numbers[index + 1]
            numbers[index] = result
            numbers.pop(index + 1)
            operations.pop(index)
        elif "-" in operations:
            index = operations.index("-")
            result = numbers[index] - numbers[index + 1]
            numbers[index] = result
            numbers.pop(index + 1)
            operations.pop(index)
    return numbers[0]
print(calculator(string))

