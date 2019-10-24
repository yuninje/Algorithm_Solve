
def dfs(n,r):
    if dp[n][r] != -1:
        return dp[n][r]

T = int(input())
dp = [[0] for _ in range(1000001)]
