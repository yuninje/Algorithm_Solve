# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD

def dfs(r,c):
    if r == N-1 and c == N-1:
        return
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if 0 <= rr and rr < N and 0 <= cc and cc < N and dp[rr][cc] > dp[r][c] + int(Map[rr][cc]):
            dp[rr][cc] = dp[r][c]+int(Map[rr][cc])
            dfs(rr,cc)
        


T = int(input())
dp = [[999999999] * 100 for _ in range(100)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]
for test in range(1,T+1):
    N = int(input())
    Map = [input() for _ in range(N)]
    for r in range(N):
        for c in range(N):
            dp[r][c] = 999999999
    dp[0][0] = 0
    dfs(0,0)
    print('#' +  str(test) + ' ' + str(dp[N-1][N-1]))
