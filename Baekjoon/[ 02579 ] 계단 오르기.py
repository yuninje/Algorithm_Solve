N = int(input())
stair = [0]
for _ in range(0,N):
    stair.append(int(input()))

dp = [0]
dp.append(stair[1])
if N >1:
    dp.append(stair[1] + stair[2])
for n in range(3,N+1):
    dp.append(max(dp[n-2] + stair[n] , dp[n-3] + stair[n-1] + stair[n]))

print(dp[N])