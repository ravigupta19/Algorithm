n = int(input())
l = [[0] for _ in range(100)]
for i in list(map(int,input().split())):
    l[i][0] = l[i][0] + 1
for i in range(n) :
    num = l[i][0]
    if num == 0:
        continue
    else:
        print_num = str(i) + ' '
        print(print_num * num, end = '')