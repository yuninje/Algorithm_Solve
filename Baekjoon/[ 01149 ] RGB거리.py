# https://www.acmicpc.net/problem/1149
# 0 : 빨, 1 : 초, 2 : 파
import sys
input = sys.stdin.readline

N = int(input())
rgb = []

for n in range(0,N):
    rgb.append(list(map(int, input().split())))

dp = [[rgb[0][0], rgb[0][1], rgb[0][2]]]
for n in range(1,N):
    dp.append([0,0,0])
for n in range(1,N):
    dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + rgb[n][0]
    dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + rgb[n][1]
    dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + rgb[n][2]


print(min(dp[N-1]))