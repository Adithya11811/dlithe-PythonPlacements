#2. write a program to count the unique value in a list

li = [4,2,2,5,3,5,2,4,1,7,8]

m = max(li)

temp = []
for i in range(m+1):
    temp.append(0)
    
for i in range(len(li)):
    temp[li[i]]+=1

cnt = 0
for i in range(m):
    if temp[i] == 1:
        cnt+=1

print(cnt)