n = 5

for i in range(0, n):
    for j in range(0, n):
        if n-i-1>=j:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()