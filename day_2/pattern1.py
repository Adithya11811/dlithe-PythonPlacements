m = int(input("Enter the number of rows"))
n = int(input("Enter the number of columns"))
for i in range(0, m):
    nstr = ""
    if i < n:
        for j in range(0, n):
            nstr += "* "
            if i == j:
                break

    print(nstr)


