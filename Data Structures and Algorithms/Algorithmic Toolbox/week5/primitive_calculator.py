#Uses python3
import sys

def optimal_sequence(n):
    values = [0, 0]

    for i in range(2, n + 1):
        increment = values[i - 1] + 1
        if i % 2 == 0:
            div2 = values[i // 2] + 1
        else:
            div2 = n + 1
        if i % 3 == 0:
            div3 = values[i // 3] + 1
        else:
            div3 = n + 1
        values.append(min(increment, div2, div3))

    sequence = [n]
    while n > 1:
        if values[n - 1] == values[n] - 1:
            n -= 1
        elif (n % 2 == 0) and values[n // 2] == values[n] - 1:
            n = n // 2
        elif (n % 3 == 0) and values[n // 3] == values[n] - 1:
            n = n // 3
        sequence.append(n)
    return(reversed(sequence))

input = sys.stdin.read()
n = int(input)
# n = 96234
# n = 1
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')