def genFibo():
    fibo_1 = 0
    fibo_2 = 1

    while True:
        next = fibo_1 + fibo_2
        yield next
        fibo_1 = fibo_2
        fibo_2 = next


nextFibonacci = genFibo()
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())
print(nextFibonacci.__next__())


