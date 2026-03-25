num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

print(num, "is an even number." if num % 2 == 0 else num, "is an odd number.")