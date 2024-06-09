n=5
for i in range(0, n):
    for j in range(0, n):
        if i == 0 or n-i == 1:
            print("*", end=" ")
        else:
            if j == 0 or n-j ==1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

