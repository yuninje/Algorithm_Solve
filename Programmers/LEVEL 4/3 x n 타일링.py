def solution(N):
    dp = [0, 0, 3,0,11]
    for n in range(5,N+1):
        if n % 2 == 1:
            dp.append(0)
            continue
        dp.append((dp[n-2] * 4 - dp[n-4]) % 1000000007)
    
    return dp[N]