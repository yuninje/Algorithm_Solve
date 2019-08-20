# https://www.acmicpc.net/problem/5557
N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(0, N-1)]

dp[0][arr[0]] = 1

for r in range(1,N-1):
    for c in range(0,21):
        if c - arr[r] >= 0:
            dp[r][c] += dp[r-1][c-arr[r]]
        if c + arr[r] <= 20:
            dp[r][c] += dp[r-1][c+arr[r]]

print(dp[N-2][arr[-1]])
