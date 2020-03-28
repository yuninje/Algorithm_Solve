# https://www.acmicpc.net/problem/11060
# 1 <= N <= 1,000
# 0 <= arr[i] <= 100

import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline
INF = 999999999
def dfs(i):
    if i == N-1 :
        return 0
    if dp[i] == -2:
        v = arr[i]
        if v == 0:
            return -1
            
        MIN = INF
        for j in range(1,v+1):
            ij = dfs(min(i+j, N-1))
            if ij == -1:
                continue
            MIN = min(MIN, ij+1)

        if MIN == INF:
            MIN = -1
        dp[i] = MIN

    return dp[i]


N = int(I())
arr = list(map(int, I().split()))
dp = [-2] * N
print(dfs(0))