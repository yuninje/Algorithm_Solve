# https://www.acmicpc.net/problem/2293
# 1 <= N <= 100
# 1 <= K <= 10,000
# 1 <= COIN(n) <= 100,000

N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(K+1)]
for a in coins:
    dp[1][a] = 1

for n in range(1,K):
    for v in range(K):
        if dp[n][v] != 0:
            for c in coins:
                if v+c <= K:
                    dp[n+1][v+c] += dp[n][v]




for d in dp:
    print(d)