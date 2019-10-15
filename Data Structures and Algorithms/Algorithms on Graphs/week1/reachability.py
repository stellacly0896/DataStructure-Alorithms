#Uses python3

import sys

traversed = []
def reach(adj, x, y):
    global traversed
    traversed = len(adj) * [False]
    explore(adj,x)
    if traversed[y]:
        return 1
    else:
        return 0
    
def explore(adj,v):
    global traversed
    traversed[v] = True
    for w in adj[v]:
        if not traversed[w]:
            explore(adj,w)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
