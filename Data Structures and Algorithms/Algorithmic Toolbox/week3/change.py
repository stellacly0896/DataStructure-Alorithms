# Uses python3
import sys

def get_change(m):
    coins = 0
    coins += int(m/10)
    m = m % 10
    coins += int(m/5)
    m = m % 5
    coins += m
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
