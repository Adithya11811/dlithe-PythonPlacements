# 4. extract elements with a freq greater than k

li = [4,2,2,5,3,5,2,4,4,1,7,8]
k = 2
#method-1
new_l = []
for i in li:
    freq = li.count(i)
    if freq>2 and i not in new_l:
        new_l.append(i)

print(new_l)
#method-2
# m = max(li)

# temp = []
# for i in range(m+1):
#     temp.append(0)
    
# for i in range(len(li)):
#     temp[li[i]]+=1

# nli = []
# for i in range(m+1):
#     if temp[i]>2:
#         nli.append(i)

# print(nli)