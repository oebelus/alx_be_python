size = input("Enter the size of the pattern: ")

for i in range(1, int(size) + 1):
    for j in range(1, int(size) + 1):
        print("*", end="")
    print()