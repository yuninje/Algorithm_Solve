# https://www.acmicpc.net/problem/11057
N = int(input())

dp = [[0 for __ in range(0,10)] for _ in range (0,N+1)]

for i in range(1,N+1):
    dp[i][0] = 1

for i in range(1,N+1):
    for j in range(1,10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

# for d in dp:
#     print(d)

print(sum(dp[N])%10007)