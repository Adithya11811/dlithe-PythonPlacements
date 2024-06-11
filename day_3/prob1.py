# 1. count the number of occurences of an item in the list

li = [4,2,2,5,3,5,2,4,1,7,8]
k = 2
cnt = 0

for x in li:
    if k == x:
        cnt+=1

print(cnt)