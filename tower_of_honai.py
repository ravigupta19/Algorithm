def printMove(fr,to):
    print('Move from ' + str(fr) + ' To ' + str(to))

def towerOfHanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr,to)
    else:
        towerOfHanoi(n-1,fr,spare,to)
        towerOfHanoi(1,fr,to,spare)
        towerOfHanoi(n-1,spare,to,fr)


print(towerOfHanoi(4,'p1','p2','p3'))