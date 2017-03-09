def gen_Primes():
    primeList = []
    starPoint = 1
    while True:
        starPoint += 1
        isPrime = True
        for prime in primeList:
            if starPoint % prime == 0:
                isPrime = False
                break
            else:
                continue
        if isPrime:
            yield starPoint
            primeList.append(starPoint)

# Note that our solution makes use of the for/else clause, which
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last