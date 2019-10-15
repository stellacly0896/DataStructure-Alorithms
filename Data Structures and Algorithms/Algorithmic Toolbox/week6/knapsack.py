# Uses python3
import sys

def optimal_weight(W, weights):
    values = weights
    cols = W + 1
    rows = len(weights) + 1

    T = [[0 for _ in range(cols)]for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i-1]:
                T[j][i] = T[j][i - 1]
            else:
                T[j][i] = max(T[j][i-1], T[i-1][j-weights[i-1]] + values[i-1])

    return T[cols-1][rows-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
