# https://www.acmicpc.net/problem/1890
# 4 <= N ( 게임판의 크기 ) <= 100
# 0 <= arr[r][c] <= 9
# arr[N-1][N-1] = 0
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def dfs(r,c):
    dp[r][c] = 0
    for d in dir:
        rr = r + d[0] * arr[r][c]
        cc = c + d[1] * arr[r][c]
        if N > rr and rr >= 0 and N > cc and cc >= 0:
            if dp[rr][cc] == -1:
                dfs(rr,cc)
            dp[r][c] += dp[rr][cc]

dir = [[1,0], [0,1]]
N = int(input())
arr = [list(map(int, I().split())) for _ in range(0,N)]
dp = [[-1] * N for _ in range(0,N)]

dp[N-1][N-1] = 1
dfs(0,0)

for d in dp:
    print(d)

