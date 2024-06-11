# 10. find a peak element in a list of integers. peak element is an element that is greater than or equal to it's neighbors

li = [1,9,8,3,5,21,7,4,17,14,6,1,2,2]

nl = []

for i in range(1,len(li)-1):
    if li[i-1] <= li[i] and li[i+1]<=li[i]:
        nl.append(li[i])

print(nl)