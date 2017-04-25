l = [[0] for _ in range(100)]
for i in list(map(int,input().split())):
    l[i][0] = l[i][0] + 1
print(' '.join(str(item) for i in l for item in i))