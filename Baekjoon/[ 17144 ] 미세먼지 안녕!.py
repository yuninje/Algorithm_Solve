# https://www.acmicpc.net/problem/17144
# 6 <= R 
# C <= 50
# 1 <= T <= 1000
# A[r,c] // 5

def wind():
    #===================위쪽=======================
    # 좌
    for r in range(up-1, 0, -1):
        origin[r][0] = origin[r-1][0]

    # 상
    for c in range(0,C-1):
        origin[0][c] = origin[0][c+1]

    # 우
    for r in range(0, up):
        origin[r][C-1] = origin[r+1][C-1]

    # 하
    for c in range(C-1, 1, -1):
        origin[up][c] = origin[up][c-1]
    
    origin[up][1] = 0
    #===================아래쪽=======================
    # 좌
    for r in range(down+1, R-1):
        origin[r][0] = origin[r+1][0]
    # 하
    for c in range(0, C-1):
        origin[R-1][c] = origin[R-1][c+1]
    # 우
    for r in range(R-1, down,-1):
        origin[r][C-1] = origin[r-1][C-1]
    # 상
    for c in range(C-1, 1, -1):
        origin[down][c] = origin[down][c-1]

    origin[down][1] = 0

def spray():
    for r in range(R):
        for c in range(C):
            if origin[r][c] != 0 and origin[r][c] != -1:
                count = 0
                o = origin[r][c]
                for dr, dc in dir:
                    rr = r + dr
                    cc = c + dc
                    if R > rr and rr >= 0 and C > cc and cc >= 0 and origin[rr][cc] != -1:
                        after[rr][cc] += o // 5
                        count += 1
                after[r][c] += o - count * (o//5)
                
dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C, T = list(map(int, input().split()))
origin = [list(map(int, input().split())) for _ in range(R)]
up = 0
down = 0

for r in range(R):
    if origin[r][0] == -1:
        up = r
        down = r+1
        break

for t in range(T):
    after = [[0] * C for _ in range(R)]
    after[up][0] = -1
    after[down][0] = -1
    spray()
    origin = after
    wind()
    
SUM = 0
for o in origin:
    SUM += sum(o)
print(SUM+2)