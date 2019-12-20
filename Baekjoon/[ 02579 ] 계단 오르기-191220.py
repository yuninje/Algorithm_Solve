# https://www.acmicpc.net/problem/2579
# 0 <= N <= 300
# 0 <= stair[n] <= 10,000
N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = stair[0]
for n in range(1,N):
    dp[n] = max(dp[n-2], dp[n-3] + stair[n-1]) + stair[n]
print(dp[-1])