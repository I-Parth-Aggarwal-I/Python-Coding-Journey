n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("Before swapping: n1 =", n1, "and n2 =", n2)

# temp
n3 = n1
n1 = n2
n2 = n3
print("After swapping: n1 =", n1, "and n2 =", n2)

# without temp
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("After swapping without temp: n1 =", n1, "and n2 =", n2)

# using function
def swap(a, b):
    return b, a
n1, n2 = swap(n1, n2)
print("After swapping using function: n1 =", n1, "and n2 =", n2)