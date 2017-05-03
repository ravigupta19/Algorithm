def Partition(arr,start,end):
    pivot = end
    partIndex = start
    for i in range(start,end):
        if arr[i] <= arr[pivot]:
            arr[i],arr[partIndex] = arr[partIndex],arr[i]
            partIndex += 1
    arr[partIndex],arr[end] = arr[end],arr[partIndex]
    return partIndex

def QuickSort(arr,start, end):
    if start < end:
        partIndex = Partition(arr,start,end)
        QuickSort(arr,start,partIndex - 1)
        QuickSort(arr, partIndex + 1, end)

arr = [2,5,8,7,9,12,3,4,6]
QuickSort(arr,0,len(arr)-1)
print(arr)