# https://www.acmicpc.net/problem/10159

def dfs(now, n, size):
    global count
    for i in range(1,N+1):
        if visit[i]:
            continue
        if inner[now][i] == size:
            visit[i] = True
            count += 1
            dfs(i, n, size)

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
inner = [[0] * (N+1) for _ in range(N+1)]
for a in arr:
    inner[a[0]][a[1]] = 8   # 무거움
    inner[a[1]][a[0]] = 1   # 가벼움

for n in range(1,N+1):
    visit = [False] * (N+1)

    count = 0
    dfs(n,n,8)
    dfs(n,n,1)
    print(N-count-1)
