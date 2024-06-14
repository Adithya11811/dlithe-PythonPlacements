def quick_sort(arr):
    if len(arr)<=1:
        return arr
    piv = arr[len(arr)//2]
    left = [x for x in arr if x<piv]
    mid = [x for x in arr if x == piv]
    right = [x for x in arr if x > piv]

    return quick_sort(left) + mid + quick_sort(right)

arr = [12,11,23,5,6,3]
print("Given Array is ", arr)
arr = quick_sort(arr)
print("Sorted array is", arr)

