# https://www.acmicpc.net/problem/2455

arr = [list(map(int, input().split())) for _ in range(0,4)]

dp = [0] * 4
dp[0] = arr[0][1]
MAX = dp[0]
for a in range(1,4):
    dp[a] = dp[a-1] - arr[a][0] + arr[a][1]
    MAX = max(dp[a], MAX)
print(MAX)