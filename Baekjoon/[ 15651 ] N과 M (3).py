# https://www.acmicpc.net/problem/15651
# 1 <= M <= N <= 7

def dfs(n, count):
    if count == M:
        print(' '.join(list(map(str, arr))))
        return

    for i in range(1,N+1):
        arr[count] = i
        
        dfs(i, count+1)
        
        arr[count] = 0
    
N, M = map(int, input().split())
arr = [0] * M
dfs(0,0)