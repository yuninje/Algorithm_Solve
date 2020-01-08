# https://www.acmicpc.net/problem/1753
# 1 <= N ( 정점 ) <= 20000
# 1 <= L ( 간선 ) <= 300000
import sys
from queue import PriorityQueue
I = sys.stdin.readline

def fun():
    dist = [INF] * (N+1)
    que = PriorityQueue()
    que.put((0,S))
    dist[S] = 0
    while not que.empty():
        d, now = que.get()
        for key in adj[now]:
            if dist[key] <= d + adj[now][key]:
                continue
            dist[key] = d + adj[now][key]
            que.put((dist[key], key)) 
    del dist[0]
    return dist

N, L = list(map(int, I().split()))
S = int(I())
adj = [dict() for _ in range(N+1)]
for i in range(L):
    a,b,d = map(int, I().split())
    if b in adj[a]:
        adj[a][b] = min(adj[a][b], d)
    else:
        adj[a][b] = d
    
INF = 999999999
for i in fun():
    if i == INF:
        print('INF')
    else:
        print(i)