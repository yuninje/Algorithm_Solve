# https://www.acmicpc.net/problem/1753
# 1 <= N ( 정점 ) <= 20000
# 1 <= L ( 간선 ) <= 300000

N, L = list(map(int, input().split()))
S = int(input())
arr = [list(map(int, input().split())) for _ in range(L)]
dp = [11] * (N+1)
adj = [[] for _ in range(N+1)]
for a, b, v in arr:
    adj[a].append((b,v))
    
