#triangle pattern
n = 5
for i in range(n):
    print("* "*(i+1))

print("\n")

for i in range(n):
    print("  "*(n-1-i) + "* "*(i+1))

#pyramid pattern

print("\n")

for i in range(n):
    print(" "*int(n-1-i) + "* "*(i+1))

#Inverted pyramid pattern

print("\n")

for i in range(n,0,-1):
    print(" "*int(n-i) + "* "*(i))
