N  = int(input())

grape = [0]
for _ in range(0,N):
    grape.append(int(input()))

dp = []
dp.append(0)#
dp.append(grape[1]) # 1
dp.append(grape[2] + grape[1]) # 2
for i in range(3,N+1):
    dp.append(max(dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i] ,dp[i-1])) # 3~N

print(dp[N])