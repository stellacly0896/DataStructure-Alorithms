#Uses python3

import sys

def explore(adj,traversed,cyc,v):
    traversed[v] = True
    cyc[v] = True
    
    for node in adj[v]:
        if traversed[node] == False:
            if explore(adj,traversed,cyc,node) == True:
                return 1
        elif cyc[v] == True:
            return 1
    cyc[v] = False
    return 0
            
def acyclic(adj):
    traversed = cyc = [False] * len(adj)
    for i in range(len(adj)):
        if traversed[i] == False:
            if explore(adj,traversed,cyc,i) == True:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
