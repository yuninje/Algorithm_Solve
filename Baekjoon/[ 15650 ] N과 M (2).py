# https://www.acmicpc.net/problem/15650
# 1 <= M <= N <= 8

def dfs(n, count):
    if count == M:
        for i in range(N+1):
            if visit[i]:
                print(i, end=' ')
        print()
        return
    if n > N:
        return
    visit[n] = True
    dfs(n+1, count+1)
    visit[n] = False
    dfs(n+1, count)

N, M = map(int, input().split())
visit = [False] * (N+1)
dfs(1,0)