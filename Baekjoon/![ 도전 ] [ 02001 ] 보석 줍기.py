# https://www.acmicpc.net/problem/2001
# 1 <= N <= 100
# 1 <= M <= 1,000
# 1 <= K <= 14
import sys
from queue import PriorityQueue

I = sys.stdin.readline


def bfs():
    pq = PriorityQueue()
    pq.put((-15, 1))
    visit = [-2] * (N+1)
    while not pq.empty():
        v, now = pq.get()
        if visit[now] != -2:
            continue
        visit[now]= -v
        for n in range(1,N+1):
            if visit[n] != -2:
                continue
            if adj[now][n] == -1:
                continue
            pq.put((max(v, -adj[now][n]), n))

    pq = PriorityQueue()
    for j in jewelry:
        pq.put(visit[j])
    count = 0
    while not pq.empty():
        v = pq.get()
        if v == -2:
            continue
        count = min(count+1, v)
    return count

N, M, K = map(int, I().split())
jewelry = [int(I().strip()) for _ in range(K)]
bridges = [list(map(int, I().strip().split())) for _ in range(M)]
adj = [[-1] * (N+1) for _ in range(N+1)]
for a, b, c in bridges:
    adj[a][b] = c
    adj[b][a] = c
print(bfs())