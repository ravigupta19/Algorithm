def Merge(left,right):
    res = []
    i, j = 0,0

    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else :
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right(i))
        j += 1

def MergeSort(n):
    if len(n) < 2:
        return n[:]
    else:
        middle = len(n) // 2
        left = MergeSort(n[:middle])
        right = MergeSort(n[middle:])
        return Merge(left,right)
