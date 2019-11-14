# https://www.acmicpc.net/problem/4485
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline
def dfs(r,c):
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if not (0 <= rr < N and 0 <= cc < N) or dp[rr][cc] <= dp[r][c] + Map[rr][cc]:
            continue
        dp[rr][cc] = dp[r][c] + Map[rr][cc]
        dfs(rr,cc)

MAX = 125
INF = 999999999
Map = [[0] * MAX for _ in range(MAX)]
dp = [[INF] * 125 for _ in range(125)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]
for test in range(1,126):
    N = int(I())
    if N == 0:
        break
    for r in range(N):
        line = list(map(int, I().split()))
        for c in range(N):
            Map[r][c] = line[c]

    for r in range(N):
        for c in range(N):
            dp[r][c] = INF

    dp[0][0] = Map[0][0]
    
    dfs(0,0)

    print('Problem ' + str(test) + ': ' + str(dp[N-1][N-1]))