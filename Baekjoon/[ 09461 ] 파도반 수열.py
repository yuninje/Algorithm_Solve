# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline
T = int(input())
dp = [0,1,1,1,2,2]
N_arr = []
for test in range(1,T+1):
    N_arr.append(int(input()))

for i in range(6, max(N_arr)+1):
    dp.append(dp[i-1] + dp[i-5])

for N in N_arr:
    print(dp[N])