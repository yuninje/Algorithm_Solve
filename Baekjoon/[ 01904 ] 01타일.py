# https://www.acmicpc.net/problem/1904
# N <= 1,000,000
N = int(input())
dp = []
dp.append(0)
dp.append(1)
dp.append(2)
for n in range(3,N+1):
    dp.append((dp[n-1] + dp[n-2])%15746)

print(dp[N])