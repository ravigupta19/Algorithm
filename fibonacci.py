def fibaRec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibaRec(n-1) + fibaRec(n-2)


print(fibaRec(5))