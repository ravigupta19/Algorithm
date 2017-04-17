def BubbleSort(n):
 for i in range(len(n),0,-1):
     for j in range(0,i-1):
         if n[j] > n[j+1]:
             (n[j],n[j+1]) = (n[j+1],n[j])

n = [4, 6, 5, 9, 8, 2, 4, 7]
BubbleSort(n)
print(n)