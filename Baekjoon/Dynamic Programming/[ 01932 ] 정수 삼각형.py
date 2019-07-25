# https://www.acmicpc.net/problem/1932
def Max(a, b):
    if a >= b:
        return a
    else:
        return b

N = int(input())

tri = []
for i in range(0,N):
    tri.append(list(map(int, input().split())))

dp = []
dp.append([0])  # dp[0]
dp.append([0,0])    # dp[1]

for n in range (2, N+2): # dp[2] ~ dp[N+1]
    dp_line = [0]
    for i in range(1,n):
        #dp[n][i] = Max(dp[n-1][i-1], dp[n-1][i])
        dp_line.append(Max(dp[n-1][i-1], dp[n-1][i])+tri[n-2][i-1])
    dp_line.append(0) 
    dp.append(dp_line)

print(max(dp[N+1]))