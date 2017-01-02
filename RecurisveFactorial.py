fact_num = input("Enter the num for which you want calculate the factorial")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(int(fact_num))

print("Your Results is :" +str(res))