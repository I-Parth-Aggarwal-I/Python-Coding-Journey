#n1 = float(input("Enter the first number: "))
#n2 = float(input("Enter the second number: "))
#n3 = float(input("Enter the third number: "))

n1, n2, n3 = map(float, input("Enter three numbers separated by spaces: ").split())

if n1 >= n2 and n1 >= n3:
    print(n1, "is the largest number.")
elif n2 >= n1 and n2 >= n3:
    print(n2, "is the largest number.")
else:
    print(n3, "is the largest number.")