# 3. find out the duplicate removal list product using list comprehension
li = [4,2,2,5,3,5,2,4,1,7,8]

res = []
[res.append(x) for x in li if x not in res]

def product(li):
    prod = 1
    for x in li:
        prod *=x

    return prod

print(res)
ans = product(res)
print(ans)