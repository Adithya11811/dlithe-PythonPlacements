for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 or 5-i == 1:
            print("*", end=" ")
        else:
            if j == 0 or 5-j ==1 or i == j or 5-i-1 == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()