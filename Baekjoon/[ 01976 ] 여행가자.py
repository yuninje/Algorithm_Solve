# https://www.acmicpc.net/problem/1976

def dfs(n, idx):
    for a in adj[n]:
        if group[a] != -1:
            continue
        group[a] = idx
        dfs(a, idx)

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
idx = 0

for n in range(N):
    if group[n] == -1:
        dfs(n, idx)
        idx += 1

for i in range(M-1):
    if group[plan[i]] != group[plan[i+1]]:
        print('NO')
        break
else:
    print('YES')

