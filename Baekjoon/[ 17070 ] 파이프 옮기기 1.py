# https://www.acmicpc.net/problem/17070
# N * N
# (r,c)  1부터 시작
# 파이프는 빈칸만
# →, ↘, ↓
# 45도만 회전
# 3 <= N <= 16
# 0 : 빈칸, 1 : 벽

def dfs(r, c, a):
    global ANSWER
    dp[r][c][a] = 0

    if a == 0 or a == 1:  # 우, 하
        # [r][cc][0] or [rr][c][1]
        rr = r + dir[a][0]
        cc = c + dir[a][1]
        if N > cc and  N > rr and arr[rr][cc] == 0:
            if dp[rr][cc][a] == -1:
                dfs(rr, cc, a)
            dp[r][c][a] += dp[rr][cc][a]

        # [rr][cc][2]
        rr = r + 1
        cc = c + 1
        if N > rr and N > cc and arr[rr][c] == 0 and arr[r][cc] == 0 and arr[rr][cc] == 0:
            if dp[rr][cc][2] == -1:
                dfs(rr, cc, 2)
            dp[r][c][a] += dp[rr][cc][2]
    elif a == 2:  # a == 2
        rr = r + 1
        cc = c + 1
        # [r][cc][0]
        if N > cc and arr[r][cc] == 0:
            if dp[r][cc][0] == -1:
                dfs(r, cc, 0)
            dp[r][c][a] += dp[r][cc][0]

        # [rr][c][1]
        if N > rr and arr[rr][c] == 0:
            if dp[rr][c][1] == -1:
                dfs(rr, c, 1)
            dp[r][c][a] += dp[rr][c][1]

        # [rr][cc][2]
        if N > rr and N > cc and arr[rr][c] == 0 and arr[r][cc] == 0 and arr[rr][cc] == 0:
            if dp[rr][cc][2] == -1:
                dfs(rr, cc, 2)
            dp[r][c][a] += dp[rr][cc][2]


dir = [[0, 1], [1, 0]]
#    →      ↓
N = int(input())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dp = [[[-1,-1,-1] for _ in range(0,N)] for _ in range(0, N)]
dp[N-1][N-1] = [1,1,1]

dfs(0, 1, 0)
print(dp[0][1][0])

