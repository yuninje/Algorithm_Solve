# https://www.acmicpc.net/problem/1912
import sys
I = sys.stdin.readline

N = int(I())
arr = list(map(int,I().split()))
dp = [int(0)] * N

dp[0] = arr[0]
MAX = arr[0]
for n in range(1,N):
    dp[n] = max(dp[n-1] + arr[n], arr[n])
    if MAX < dp[n]:
        MAX = dp[n]
print(MAX)
