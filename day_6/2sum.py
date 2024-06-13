# Given an array of n numbers and another number the task is to check whether or not there exists 2 elements in array whose exact sum is x
def two_sum(arr, x):
    # pass
    target = x//2
    i = 0
    li = []
    while arr[i]<target:
        d=x-arr[i]
        if d in arr:
            li.append((arr[i], int(d)))
        i+=1
    return li

arr = [9,4,2,6,3,23,5,8,0]
x = 8
arr.sort()
li = two_sum(arr, x)
if len(li) == 0:
    print("no pair possible")
else:
    print("pairs are: ", li)

#without sort

def t_s_without_sort(arr, target):
    n = len(arr)
    li = []
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if target-arr[i] == arr[j]:
                li.append((min(arr[i],arr[j]), max(arr[i],arr[j])))

    return li

li = list(set(t_s_without_sort(arr, x)))
if len(li) == 0:
    print("no pair possible")
else:
    print("pairs are: ", li)






