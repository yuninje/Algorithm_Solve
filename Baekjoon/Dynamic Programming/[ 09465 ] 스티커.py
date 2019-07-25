# https://www.acmicpc.net/problem/9465
T = int(input())

for test in range(1,T+1):
    N = int(input())
    arr = []    
    dp = []

    for i in range(0,2):
        arr.append(list(map(int,input().split())))
        dp.append([0 for _ in range(0,N)])
    dp.append([0 for _ in range(0,N)])

    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1] + arr[1][0]
    dp[1][0] = arr[1][0]
    dp[1][1] = arr[1][1] + arr[0][0]
    dp[2][0] = max(dp[1][0], dp[0][0])
    dp[2][1] = max(dp[1][1], dp[0][1])

    for i in range(2,N):
        dp[0][i] = max(dp[1][i-1] + arr[0][i], dp[1][i-2] + arr[0][i])
        dp[1][i] = max(dp[0][i-1] + arr[1][i], dp[0][i-2] + arr[1][i])
        dp[2][i] = max(dp[0][i], dp[1][i])

    print(dp[2][N-1])