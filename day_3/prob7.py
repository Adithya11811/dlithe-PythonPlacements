#7. write a program to merge to sorted list into a single sorted list

l1 = [1,3,5,7]
l2 = [2,6,10]

i,j = 0,0
res = []

n1 = len(l1)
n2 = len(l2)

while i <= n1-1 and j<=n2-1:
    if l1[i] < l2[j]:
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1

if i > n1-1:
    res.extend(l2[j:])
else:
    res.extend(l1[i:])

print(res)