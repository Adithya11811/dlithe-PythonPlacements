# 8. find the largest subarray sum of a given list

li = [-11,2,2,-3, 4,12,-13]
li=[1,2,3,4]
maxi=0
n = len(li)+1
for subarr in range(1, n+1):
    for i in range(0, n-subarr+1):

        res = li[i: i+subarr]
        val =sum(res)
        if maxi < val:
            maxi =val

print(maxi)
