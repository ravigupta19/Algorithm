def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range (1, len(L)):
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                swap = False


L = [0,4,2,8,9,6,5,10]
bubble_sort(L)
print(L)

# Complexity of bubble sort is O(n ^ 2)
