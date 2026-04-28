from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest, max_dist = start, 0
    while q:
        node = q.popleft()
        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)
                if dist[nei] > max_dist:
                    max_dist = dist[nei]
                    farthest = nei
    return farthest, max_dist

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

u, _ = bfs(1, adj, n)
v, diameter = bfs(u, adj, n)

print(diameter * 3)