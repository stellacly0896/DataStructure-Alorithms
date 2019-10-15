# Uses python3
import sys
from math import inf

def get_change(m):
    deno = [1,3,4]
    MinNumCoins = [float("inf")] * (m+1)
    MinNumCoins[0] = 0

    for i in range(1,m+1):
        for j in deno:
            if i >= j:
                coins = MinNumCoins[i-j] + 1
                if coins < MinNumCoins[i]:
                    MinNumCoins[i] = coins
    return MinNumCoins[m]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
