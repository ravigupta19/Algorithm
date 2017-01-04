def efficent_fibonacci(d,n):

    if n in d:
        return d[n]
    else:
         ans = efficent_fibonacci(d, n-1) + efficent_fibonacci(d, n-2)
         d[n] = ans
         return ans

def fibonacci(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 34
d = {1:1,2:2}

print('using efficent fib')
print(efficent_fibonacci(d,n))
print('using fib')
print(fibonacci(n))