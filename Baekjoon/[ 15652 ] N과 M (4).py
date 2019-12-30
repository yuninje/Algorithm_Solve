# https://www.acmicpc.net/problem/15652
# 1 <= M <= N <= 8
# A[1] <= A[2] <= A[3] ... <= A[M]

def dfs(before, n, count):
    if count == M:
        print(' '.join(list(map(str, arr))))
        return
    
    for i in range(1,N+1):
        if before <=  i:
            arr[count] = i
            dfs(i, n+1, count+1)
            arr[count] = 0

N, M = map(int, input().split())
arr = [0] * (M)
dfs(0, 0, 0)