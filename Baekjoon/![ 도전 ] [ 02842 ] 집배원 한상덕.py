# https://www.acmicpc.net/problem/2842
# P : 우체국
# K : 집
# . : 목초지
# 우체국 ~   ~ 우체국
# 2 <= N <= 50
# 

import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def bfs(now):
    queue = [[home[now][0], home[now][1]]]
    home_count = 0
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]

            if arr[r][c] == 'K' or arr[r][c] == 'P':
                home_count += 1
                for h in range(0,home_len):
                    if r == home[h][0] and c == home[h][1]:
                        inner[now][h] = dp[r][c]
                        inner[h][now] = dp[r][c]
                        break
                if home_count == home_len-1:
                    return
            dp[r][c][0] = max(height[r][c], dp[r][c][0])
            dp[r][c][1] = min(height[r][c], dp[r][c][1])
            for d in dir:
                rr = r+d[0]
                cc = c+d[1]
                if N > rr and rr >= 0 and N > cc and cc >= 0:
                    dp[rr][cc][0] = min(dp[r][c][0], dp[rr][cc][0])
                    dp[rr][cc][1] = max(dp[r][c][1], dp[rr][cc][1])

                    if visit[rr][cc] :
                        continue
                    visit[rr][cc] = True
                    queue_.append([rr,cc])
            
        queue = queue_


dir = [[1,1], [1,-1], [1, 0], [-1, 1], [-1,0], [-1,-1], [0,1], [0,-1]]
N = int(I())
arr = []
height = []
home = []
for r in range(0,N):
    arr.append(I())
    for c in range(0,N):
        if arr[r][c] == 'K':
            home.append([r,c])
        elif arr[r][c] == 'P':
            start = [r,c]
home.append(start)
home_len = len(home)

for n in range(0,N):
    height.append(list(map(int, I().split())))

inner = [[[0,0]] * home_len for _ in range(0,home_len)]

for h in range(0,home_len-1):
    visit = [[False] * N for _ in range(0,N)]
    visit[home[h][0]][home[h][1]] = True
    dp = [[[0,10000001]] * N for _ in range(0,N)]
    bfs(h)

for i in inner:
    print(i)
