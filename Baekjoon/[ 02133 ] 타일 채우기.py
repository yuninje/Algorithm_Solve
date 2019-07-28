# https://www.acmicpc.net/problem/2133
N = int(input())

dp = [0 for _ in range(0,N+2)]
dp[2] = 3
for d in range(4,N+1):
    if d % 2 == 0:    
        copy_d = d - 2
        while copy_d > 0 :
            if copy_d == d-2:
                dp[d] += dp[copy_d] * 3
            else:
                dp[d] += dp[copy_d] * 2
            copy_d -=2

        dp[d] += 2
print(dp[N])