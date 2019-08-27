# https://www.acmicpc.net/problem/2225

N, K = list(map(int, input().split()))

dp = [[1] * (K+1) for _ in range(0,N+1)]

for n in range(1,N+1):
    for k in range(2,K+1):
        dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % 1000000000

print(dp[n][K])
