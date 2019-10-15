# Uses python3
import sys

def fib(n):
    if n <=1:
        return n
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

def get_length(m):
    if m <= 1:
        return m
    a,b = 0,1
    for i in range(m * m + 1):
        a , b = b, ((a + b) % m)
        if a == 0 and b == 1:
            return i+1

def get_fibonacci_huge(n, m):
    remainder = n%get_length(m)
    return fib(remainder) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
