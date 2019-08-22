import sys
import copy
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def bfs(idx):
    queue = [home[idx][0], home[idx][1]]
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            
            for d in dir:
                rr = r+d[0]
                cc = c+d[1]
                if N > rr and rr >= 0 and N > cc and cc >= 0:
                    if not visit[rr][cc]:
                        visit[rr][cc] = True
                        queue_.append([rr,cc])
                    if dp[]


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
visit = [[False] * N for _ in range(0,N)]
for n in range(0,N):
    height.append(list(map(int, I().split())))

dp = [[0] * N for _ in range(0,N)]
for r in range(0,N):
    for c in range(0,N):
        dp[r][c] = [height[r][c], height[r][c]]

for h in range(0, home_len):
    bfs(h)

inner = [[[0,0]] * home_len for _ in range(0,home_len)]