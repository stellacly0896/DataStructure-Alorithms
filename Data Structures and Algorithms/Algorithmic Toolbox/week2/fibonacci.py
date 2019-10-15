# Uses python3
def calc_fib_fast(n):
    if n <=1:
        return n
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

n = int(input())
print(calc_fib_fast(n))
