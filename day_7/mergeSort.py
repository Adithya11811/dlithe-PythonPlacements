# O(nlogn)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        subArr1 = arr[:mid]
        subArr2 = arr[mid:]

        mergeSort(subArr1)
        mergeSort(subArr2)

        i = j = k = 0

        while i < len(subArr1) and j< len(subArr2):
            if subArr1[i] <subArr2[j]:
                arr[k] = subArr1[i]
                i+=1
            else:
                arr[k] = subArr2[j]
                j+=1
            k+=1
        
        while i<len(subArr1):
            arr[k] = subArr1[i]
            i+=1
            k+=1

        while j < len(subArr2):
            arr[k] = subArr2[j]
            j+=1
            k+=1

arr = [10,20,50,23,4,2]
mergeSort(arr)
print(arr)