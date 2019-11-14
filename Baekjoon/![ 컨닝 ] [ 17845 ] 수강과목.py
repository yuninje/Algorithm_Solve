# https://www.acmicpc.net/problem/17845
# 1 <= N <= 1000
# 1 <= TIME <= 10000

import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def dfs(now, time):
    if now == N:
        return 0
    if dp[now][time] == -1:
        v, t = arr[now]
        
        MAX = dfs(now+1, time)
        if time - t >= 0:
            MAX = max(MAX, dfs(now+1, time-t)+v)
        dp[now][time] = MAX

    return dp[now][time]

TIME, N = list(map(int, I().split()))
arr = [list(map(int, I().split())) for _ in range(N)]
# 중요도, 시간
dp = [[-1] * (TIME+1) for _ in range(N)]
print(dfs(0,TIME))