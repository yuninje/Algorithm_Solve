# https://www.acmicpc.net/problem/1520
# 1 <= R, C <= 500
# 1 <= arr[r][c] <= 10000
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline
def dfs(r,c):
    if r == R-1 and c == C-1:
        dp[r][c] = 1
        return
    dp[r][c] = 0
    for d in dir:
        rr = r + d[0]
        cc = c + d[1]
        if R > rr and rr >= 0 and C > cc and cc >= 0 and not visit[rr][cc] and arr[rr][cc] < arr[r][c]:
            if dp[rr][cc] == -1:
                visit[rr][cc] = True
                dfs(rr,cc)
                visit[rr][cc] = False
                dp[r][c] += dp[rr][cc]
            else:
                dp[r][c] += dp[rr][cc]


dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
arr = [list(map(int, I().split())) for _ in range(0,R)]

dp = [[-1] * C for _ in range(0,R)]
visit = [[False] * C for _ in range(0,R)]

dfs(0,0)

for d in dp:
    print(d)

print(dp[0][0])
