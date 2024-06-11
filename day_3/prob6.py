# 6. write a program to demonstrate union and intersection of Sets

l1 = [1,2,3,8,10]
l2 = [6,7,8,9]
temp = [1,2,3,8,10]

def union(l1, l2):
    nli = l1
    for x in l2:
        if x not in l1:
            nli.append(x)

    return nli

def intersection(l1,l2):
    nli = []
    for x in l2:
        if x in l1:
            nli.append(x)

    return nli

print(union(l1,l2))   
print(intersection(temp,l2))   