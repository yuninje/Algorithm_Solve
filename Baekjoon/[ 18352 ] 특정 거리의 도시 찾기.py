# https://www.acmicpc.net/problem/18352
# N : 도시의 개수
# M : 도로의 개수
# K : 거리 정보
# X : 출발 도시

import sys
I = sys.stdin.readline

def bfs(s):
    visit[s] = True
    que = [s]
    count = 0
    while que:
        if count == K:
            return sorted(que)
        que_ = []

        for q in que:
            visit[q] = True
            for a in adj[q]:
                if visit[a]:
                    continue
                visit[a] = True
                que_.append(a)
        que = que_
        count += 1
    return [-1]
N, M, K, X = map(int,  I().split())
arr = [list(map(int, I().split())) for _ in range(M)]
adj = [[] for _ in range(N+1)]

for s, e in arr:
    adj[s].append(e)

visit = [False] * (N+1)

for q in bfs(X):
    print(q)
