def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    greater = 0
    gcd = 1
    if a > b:
        greater = a
    else:
        greater = b
    for i in range (2, greater+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

print(gcdIter(9, 12))