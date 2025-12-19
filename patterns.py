n=int(input("Enter a number:"))
print("PATTERN 1")
for i in range(1,n+1):
    for j in range(n):
        print("*",end=" ")
    print()

print("PATTERN 2")
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("PATTERN 3")
for i in range(n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()

print("PATTERN 4")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

print("PATTERN 5")
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

print("PATTERN 6")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
