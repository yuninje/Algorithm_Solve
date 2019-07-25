# https://www.acmicpc.net/problem/2133
N = int(input())

dp = [0 for _ in range(0,N+1)]
dp[0] = 1
dp[2] = 3
dp[4] = 11
for d in range(6,N+1):
    if d % 2 == 0:    
        copy_d = d - 2
        while copy_d > 0 :
            dp[d] = dp[copy_d] * dp[d - copy_d]
            copy_d -= 2
        dp[d] += 2
print(dp[N]) 
            