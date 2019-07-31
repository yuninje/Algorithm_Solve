# https://www.acmicpc.net/problem/1012
# 1 <= M <= 50
# 1 <= N <= 50
# 1 <= K <= 2500
# 0 <= X <= M-1
# 0 <= Y <= N-1
# 0 : 빈공간 , 1 : 배추 , 2 : 테두리 , 3 : 확산된 배추

import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    if arr[r][c] != 1:
        return

    arr[r][c] = 3
    
    dfs(r+1,c)
    dfs(r-1,c)
    dfs(r,c+1)
    dfs(r,c-1)


T = int(input())
for test in range(1,T+1):
    M, N, K = list(map(int, input().split()))

    arr = [[2 for _ in range(0,M+2)] for __ in range(0,N+2)]
    for n in range(1,N+1):      # 1 ~ N
        for m in range(1,M+1):  # 1 ~ M
            arr[n][m] = 0
    
    for k in range(0,K):
        x, y = list(map(int, input().split()))
        arr[y+1][x+1] = 1


    answer = 0
    for r in range(1, N+1):     # 1 ~ N
        for c in range(1, M+1): # 1 ~ M
            if arr[r][c] == 1:
                dfs(r,c)
                answer += 1
    print(answer)