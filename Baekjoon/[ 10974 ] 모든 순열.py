# https://www.acmicpc.net/problem/10974
def dfs(count):
    if count == N:
        print(' '.join(list(map(str, arr))))
    
    for i in range(1,N+1):
        if visit[i]:
            continue
        visit[i] = True
        arr[count] = i
        dfs(count+1)
        visit[i] = False

N = int(input())
arr = [0] * N
visit = [False] * (N+1)
dfs(0)