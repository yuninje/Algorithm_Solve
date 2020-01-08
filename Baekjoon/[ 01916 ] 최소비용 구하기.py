# https://www.acmicpc.net/problem/1916
# 1 <= N <= 1,000
# 1 <= M <= 100,000
# 0 <= v <= 100,000

from queue import PriorityQueue
import sys

I = sys.stdin.readline

def dijkstra():
    que = PriorityQueue()
    que.put((0,A))
    dist = [INF] * (N+1)
    while not que.empty():
        v, now = que.get()
        if dist[now] != INF:
            continue
        dist[now] = v
        if now == B:
            return v   

        for i in range(1,N+1):
            if dist[i] != INF:
                continue 
            if adj[now][i] == INF:
                continue
            que.put((v + adj[now][i], i))

N = int(I())
M = int(I())
arr = [list(map(int, I().split())) for _ in range(M)]
A, B = map(int, I().split())
INF = 999999999
adj = [[INF] * (N+1) for _ in range(N+1)]
for a, b, v in arr:
    if adj[a][b] > v:
        adj[a][b] = v
print(dijkstra())