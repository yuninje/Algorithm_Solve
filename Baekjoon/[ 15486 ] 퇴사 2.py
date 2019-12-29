# https://www.acmicpc.net/problem/15486
# 1 <= N <= 1,500,000
# 1 <= T[i] <= 50
# 1 <= P[i] <= 1000
import sys
I = sys.stdin.readline
N = int(I())
arr = [list(map(int, I().split())) for _ in range(N)]
dp = [0] * (N+1)

for n in range(N-1,-1,-1):
    if n + arr[n][0] - 1 < N:
        dp[n] = max( dp[n+arr[n][0]] + arr[n][1], dp[n+1] )
    else:
        dp[n] = dp[n+1]

print(dp[0])