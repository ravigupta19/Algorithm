L = [1,2,3,4,5]

def genSubSet(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubSet(L[:-1])

    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

print(L[-1:])