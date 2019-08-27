# https://www.acmicpc.net/problem/1965

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
MAX = 0
for n in range(0,N):
    for m in range(0,n):
        if arr[n] > arr[m]:
            dp[n] = max(dp[n], dp[m])
    dp[n] += 1
    MAX = max(MAX, dp[n])
print(MAX)