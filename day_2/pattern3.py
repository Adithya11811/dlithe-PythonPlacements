for i in range(0, 5):
    nstr = ""
    for j in range(0, 5):
        if i <= j:
            nstr += "* "
        else:
            nstr+= "  "

    print(nstr)