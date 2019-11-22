# https://www.acmicpc.net/problem/17069
# 3 <= N <= 32
# 0 : 빈칸,  1 : 벽
N = int(input())
Map = [list(map(int, input().split()))+[0] for _ in range(N)]
Map.append([0] * (N+1))

dp = [[[0,0,0] for __ in range(N+1)] for _ in range(N+1)]
dp[0][1][0] = 1
for r in range(N):
    for c in range(N):
        if Map[r][c] == 1:
            continue
        if Map[r][c+1] != 1:
            dp[r][c+1][0]   += dp[r][c][0] + dp[r][c][1]
        if Map[r][c+1] != 1 and Map[r+1][c] != 1 and Map[r+1][c+1] != 1:
            dp[r+1][c+1][1] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]
        if Map[r+1][c] != 1:
            dp[r+1][c][2]   += dp[r][c][1] + dp[r][c][2]


print(sum(dp[N-1][N-1]))