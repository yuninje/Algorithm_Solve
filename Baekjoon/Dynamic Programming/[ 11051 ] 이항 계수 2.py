# https://www.acmicpc.net/problem/11051
N, K = list(map(int, input().split()))

dp = [[0 for _ in range(0,K+1)] for __ in range(0,N+1)]

for n in range(0,N+1):
    dp[n][0] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % 10007


print(dp[N][K])