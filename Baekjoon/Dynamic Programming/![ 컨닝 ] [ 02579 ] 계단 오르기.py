# https://www.acmicpc.net/problem/2579
def solution():

    return

def Max(a, b):
    if a>b:
        return a
    else:
        return b

N = int(input())
stair = []
for _ in range(0,N):
    stair.append(int(input()))

dp = []
dp.append(stair[0]) # [0]
dp.append(Max(stair[0] + stair[1], stair[1]))
dp.append(Max(stair[0]+stair[2], stair[1] + stair[2]))

for i in range(3,N):
    dp.append(Max(dp[i-2] + stair[i], stair[i-1] + stair[i] + dp[i-3]))


print(dp[N-1])