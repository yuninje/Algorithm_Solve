# https://www.acmicpc.net/problem/11727
# 1 <= n <= 1000
# answer % 10007 출력.

N = int(input())
dp = [0, 1, 3]
for i in range(3,N+1):
    dp.append((dp[i-2] * 2 + dp[i-1])%10007)

print(dp[N])