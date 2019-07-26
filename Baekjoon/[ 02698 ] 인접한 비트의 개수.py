# https://www.acmicpc.net/problem/2698
T = int(input())

for test in range(1, T+1):
    N, K = list(map(int, input().split()))

    dp = []
    for n in range(0,N+1):
        dp.append([0 for k in range(0,N+1)])
    dp[0][0] = 1

    dp[1][0] = 2
    
    dp[2][0] = 3

    for n in range(2,N+1):
        dp[n][0] = dp[n-1][0] + dp[n-2][0]
        dp[n][n-1] = 1
    
    for n in range(2,N+1):
        for k in range(1,K+1):
            dp[n][k] += dp[n-1][k]+dp[n-2][k]
            minus = 1
            while(n -minus - 2 >= 0 and k-minus>=0):
                dp[n][k] += dp[n-minus-2][k-minus]
                minus += 1

    print(str(dp[N][K]))

