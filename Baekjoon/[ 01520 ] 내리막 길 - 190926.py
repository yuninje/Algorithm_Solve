import sys

sys.setrecursionlimit(10**6)
I = sys.stdin.readline
def dfs(r,c):
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if 0 <= rr and rr < R and 0 <= cc and cc < C:
            if arr[r][c] < arr[rr][cc]:
                dp[r][c] += dfs(rr,cc)
    return dp[r][c]

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
arr = [list(map(int, I().split())) for _ in range(R)]
dp = [[-1] * C for _ in range(R)]
dp[0][0] = 1

print(dfs(R-1,C-1))