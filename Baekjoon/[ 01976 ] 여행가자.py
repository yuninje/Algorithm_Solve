# https://www.acmicpc.net/problem/1976

def dfs(n):
    group[n] = 0
    for a in adj[n]:
        if group[a] != -1:
            continue
        dfs(a)

N = int(input())
M = int(input())
adj_array =[ list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x : int(x) -1, input().split()))
adj = [ [] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj_array[i][j] == 1:
            adj[i].append(j)

group = [-1] * N

dfs(plan[0])

for p in plan:
    if group[p] == -1:
        print('NO')
        break
else:
    print('YES')