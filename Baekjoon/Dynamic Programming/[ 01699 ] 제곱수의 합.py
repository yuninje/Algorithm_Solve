N = int(input())

dp = [N+1 for _ in range(0,N+1)]
dp[0] = 0
dp[1] = 1


for i in range(2,N+1):
    for j in range(1,N):
        if i >= j*j:
            dp[i] = min(dp[i], dp[i-j*j]+1)
        else:
            break


print(dp[N])
