n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i+1, n+1):
        print("*", end="")
    print()
