def InsertionSort(n):
    for i in range(1,len(n)):
        hole = i
        value = n[i]
        while hole > 0 and n[hole-1] > value:
            n[hole] = n[hole -1]
            hole -= 1
        n[hole] = value

n = [4, 6, 5, 9, 8, 2, 4, 7]
InsertionSort(n)
print(n)



