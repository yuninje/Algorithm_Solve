# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD

T = int(input())
dir = [[1,0], [-1,0], [0,1], [0,-1]]
for test in range(1,T+1):
    N = int(input())
    Map = [list(map(int, list(input()))) for _ in range(N)]
    dp = [[999999999] * N for _ in range(N)]
    dp[0][0] = 0
    # bfs + memoization

    que = [(0,0)]

    while que:
        que_ = []
        for r, c in que:
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if 0 <= rr and rr < N and 0 <= cc and cc < N and dp[rr][cc] > dp[r][c] + Map[rr][cc]:
                    dp[rr][cc] = dp[r][c] + Map[rr][cc]
                    que_.append((rr,cc))                    

        que = que_
    
    print('#' + str(test) + ' ' + str(dp[N-1][N-1]))