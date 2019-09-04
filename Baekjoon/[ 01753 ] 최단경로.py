# https://www.acmicpc.net/problem/1753
# 1 <= N ( 정점 ) <= 20000
# 1 <= L ( 간선 ) <= 300000
import sys
I = sys.stdin.readline
N, L = list(map(int, I().split()))
S = int(I())
dp = [200001] * (N+1)
visit = [False] * (N+1)
adj = [[] for _ in range(N+1)]
for _ in range(L):
    a, b, v = list(map(int,input().split()))
    adj[a].append((b,v))

queue = [(S,0)]
while queue:
    queue = sorted(queue, key= lambda x: x[1])
    q1, v1 = queue.pop(0)
    if visit[q1]:
        continue
    dp[q1] = v1
    visit[q1] = True
    for q2, v2 in adj[q1]:
        queue.append((q2,v1 + v2))
    
del dp[0]
for d in dp:
    if d == 200001:
        print('INF')
    else:
        print(d)