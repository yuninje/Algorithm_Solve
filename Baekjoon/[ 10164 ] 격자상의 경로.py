# https://www.acmicpc.net/problem/10164
# 1 <= R, C <= 15
# 1 < K < R * C
R, C, K = list(map(int, input().split()))
if K==0:
    K = R * C
dp = [[1] * (C) for _ in range(R)]
kr = (K-1) // C
kc = (K-1) % C
for r in range (1,max(kr+1, R-kr)):
    for c in range(1,max(kc+1,C-kc)):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]

print(dp[kr][kc] * dp[R - 1 - kr][C - 1 - kc])