# https://www.acmicpc.net/problem/2011
# len(str) <= 5000
Str = input()
irr = list(map(int, list(Str)))
N = len(Str)
dp = [0] * (N+1)
dp[N-1] = 1
dp[N] = 1
for n in range(N-2, -1, -1):
    if irr[n] == 1 or (irr[n] == 2 and irr[n+1] <= 6):
        dp[n] += dp[n+2]
    dp[n] += dp[n+1]

print(dp[0])