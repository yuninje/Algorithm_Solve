# https://www.acmicpc.net/problem/1937
# 1 <= N <= 500
# 1 <= arr[r][c] =<= 1000000
import sys
sys.setrecursionlimit(10 ** 6)
I = sys.stdin.readline

def dfs(r,c):
    global MAX
    if dp[r][c] != -1:
        return

    dp[r][c] = 1
    for d in dir:
        rr = r + d[0]
        cc = c + d[1]
        if N > rr and rr >= 0 and N > cc and cc >= 0:
            if arr[r][c] > arr[rr][cc]:
                if dp[rr][cc] == -1:
                    dfs(rr,cc)
                dp[r][c] = max(dp[r][c], dp[rr][cc]+1)

    MAX = max(MAX, dp[r][c])

dir = [[1,0], [-1,0], [0,1], [0,-1]]
N = int(I())
arr = [list(map(int, I().split())) for _ in range(0, N)]
dp = [[-1] * N for _ in range(0,N)]
MAX = 0

for r in range(0,N):
    for c in range(0,N):
        dfs(r,c)
for d in dp:
    print(d)
print(MAX)