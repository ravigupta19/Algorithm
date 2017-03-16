def bubble_sort_optimize(L):
    swap = False
    n = len(L)
    while not swap:
        swap = True
        for j in range(1,n):
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                swap = False
        n -= 1

L = [0,4,2,8,9,6,5,10]
bubble_sort_optimize(L)
print(L)

# in This we have reduce the size of the L after every pass because last element of list is sorted
