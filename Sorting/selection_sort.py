def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt,len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        print(L)

L = [3,4,2,8,9,6,5,10,0]
selection_sort(L)
print(L)

#Complexity of selection sort is same as Bubble sort which is O(n ^ 2)
#In selection sort we find the smallest element swap with intial index
# and then we continue same process excluding sorted list
#