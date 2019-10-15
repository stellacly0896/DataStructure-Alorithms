#Uses python3

import sys

def find_min(visited,dist):
    min_vertex = len(dist)
    min_dist = 9999999
    
    for v in range(len(dist)):
        if not visited[v] and dist[v]< min_dist:
            min_vertex = v
            min_dist = dist[v]
    return min_vertex

def distance(adj, cost, s, t):
    l = len(adj)
    dist = [9999999] * l
    visited = [False] * l 
    dist[s] = 0
    
    for i in range(l - 1):
        v = find_min(visited,dist)
        if v == l:
            break
        visited[v] = True
        i = 0
        for u in adj[v]:
            if not visited[u] and dist[u] > dist[v]+cost[v][i]:
                dist[u] = dist[v]+cost[v][i]
            i += 1
            
    if dist[t] != 9999999:
        return dist[t]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
