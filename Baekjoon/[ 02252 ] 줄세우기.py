# https://www.acmicpc.net/problem/2252
import sys
from queue import PriorityQueue
I = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now, value):
    for i in adj[now][1]:
        if pos[i] < value+1:
            pos[i] = value+1
            dfs(i, value+1)

N, M = map(int, I().split())
arr = [list(map(int, I().split())) for _ in range(M)]

adj = [[[],[]] for _ in range(N+1)]
for a, b in arr:
    adj[a][1].append(b)
    adj[b][0].append(a)


pos = [0] * (N+1)
for i in range(1,N+1):
    if len(adj[i][0]) == 0:
        dfs(i, 0)

que = PriorityQueue()
for i in range(1,N+1):
    que.put((pos[i], i))

while not que.empty():
    print(que.get()[1], end=' ')