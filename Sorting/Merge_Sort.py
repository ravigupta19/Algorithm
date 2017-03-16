# Mergging two list

def merge(left, right):
    res = []
    i,j = 0, 0

    while i < len (left) and j < len(right):
         if left[i] < right[j]:
             res.append(left[i])
             i += 1
         else:
             res.append(right[j])
             j += 1
         print(res)

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    return res

#left = [1,5,12,18,19,20]
#right = [2,3,4,47]

L = [3,4,2,8,9,6,5,10,0]
#Complexity of merge is O(n)
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left,right)

#Complexity of merge_sort id O(logn) but merge_sort also calls merge function which have complexity of O(n)
#According to rule of mutlipcation O(O(n) * O(logn)) => O(n*logn) => O(nlogn)
print(merge_sort(L))
#print(merge(left,right))