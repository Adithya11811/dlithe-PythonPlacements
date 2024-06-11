# 5. write a program to test if a list contains elements in the range

li = [4,2,2,5,3,5,2,4,4,1,7,8]
lr = 9
hr = 12

flag = False
for i in range(len(li)):
    if li[i]>=lr and li[i] <hr:
        print("elements within the given range exists")
        flag = True
        break

if flag == False:
    print("element within range doesn't exist")
