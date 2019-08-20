# https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3
# 1 <= N <= 60000
# result % 1,000,000,007


def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])% 1000000007
    
    return dp[n]


print(solution(4)) # result : 5
