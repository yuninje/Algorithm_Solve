# https://www.acmicpc.net/problem/1753
# 1 <= N ( 정점 ) <= 20,000
# 1 <= L ( 간선 ) <= 300,000
import time
from queue import PriorityQueue

def dijkstra(s):
    dist = [INF] * (V+1)
    dist[s] = 0

    que = PriorityQueue()
    for q in adj[s]:
        que.put(q)

    while not que.empty():
        v, m = que.get()

        if dist[m] <= v:
            continue
        dist[m] = v

        for vv, e in adj[m]:
            que.put((vv+v, e))

    return dist

def make_adj():
    adj = [[] for _ in range(V+1)]
    for s, e, v in arr:
        adj[s].append((v,e))

    return adj

start = time.time()  # 시작 시간 저장
INF = 999999999
V, E = list(map(int, input().split()))
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
adj = make_adj()
dist = dijkstra(K)
del dist[0]
for d in dist:
    print(d, end=' ')
print('total time : ', time.time()-start)