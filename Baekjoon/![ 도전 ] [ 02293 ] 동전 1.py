# https://www.acmicpc.net/problem/2293
# 1 <= N <= 100
# 1 <= K <= 10,000
# 1 <= COIN(n) <= 100,000
import sys
sys.setrecursionlimit(10**6)

N, K = list(map(int, input().split()))
coins = [0]
for n in range(0,N):
    coins.append(int(input()))

dp = [[0] *(K+1) for _ in range(0,N+1)]

# for r in range (1, N+1):
#     dp[r][0] = 1
#     for c in range(1,K+1):
#         dp[r][c] = dp[r][c-coins[r]] + dp[r-1][c]
for d in dp:
    print(d)

print(dp[N][K])