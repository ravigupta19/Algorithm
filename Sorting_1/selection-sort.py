n = list(map(int,input().split()))

def Selection_sort(n):
    for i in range(len(n)):
        min = i
        for j in range(i+1,len(n)):
            if n[j] < n[min]:
                min = j
        temp = n[i]
        n[i] = n[min]
        n[min] = temp

Selection_sort(n)
print(n)