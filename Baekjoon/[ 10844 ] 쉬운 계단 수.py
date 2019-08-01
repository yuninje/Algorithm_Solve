# https://www.acmicpc.net/problem/10844
N = int(input())
dp = [[0] * 12 for _ in range(0,N)]

for i in range(2,11):
    dp[0][i] = 1


for r in range(1,N):
    for c in range(1,11):
        dp[r][c] = (dp[r-1][c-1] + dp[r-1][c+1]) % 1000000000

print(sum(dp[N-1])% 1000000000)