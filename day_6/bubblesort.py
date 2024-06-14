def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [64,27,45,1,4,6,2,89]
bubbleSort(arr)
print(arr)