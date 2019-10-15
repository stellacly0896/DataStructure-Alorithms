# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_unit = [float(values)/float(weights) for values,weights in zip(values,weights)]
    for i in range(len(weights) + 1):
        if capacity == 0:
            return value

        max_v = max(value_per_unit) #找到单价最高的那个
        index = value_per_unit.index(max_v) #找到它的index
        value_per_unit[index] = -1
        a = min(weights[index], capacity)
        value += a * max_v
        weights[index] -= a
        capacity -= a
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
