# https://www.acmicpc.net/problem/3197
# 1 <= R , C <= 1,500
# check() 의 시간을 줄이면 어떻게 될 것 같다.

import sys
I = sys.stdin.readline

def bfs(sr,sc):
    global temp

    que = [(sr,sc)]
    while que:
        que_ = []
        for r, c in que:
            Map[r][c] = '.'
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not ( 0 <= rr < R and 0 <= cc < C ):
                    continue
                if visit[rr][cc]:
                    continue

                if Map[rr][cc] == 'X':
                    temp.append((rr,cc))
                elif Map[rr][cc] == 'O':
                    que_.append((rr,cc))
                    visit[rr][cc] = True
        que = que_
    
def check():
    sr, sc = swany[0]
    er, ec = swany[1]
    for r in range(R):
        for c in range(C):
            checkVisit[r][c] = False

    que = [(sr,sc)]
    while que:
        que_ = []
        for r, c in que:
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not ( 0 <= rr < R and 0 <= cc < C ):
                    continue
                if checkVisit[rr][cc]:
                    continue
                checkVisit[rr][cc] = True
                if Map[rr][cc] == '.':
                    que_.append((rr,cc))
        que = que_

    return checkVisit[er][ec]


def fun():
    global temp
    count = 0
    while True:

        temp = []
        for r in range(R):
            for c in range(C):
                if Map[r][c] == 'O' and not visit[r][c]:
                    bfs(r,c)

        for tr, tc in temp:
            Map[tr][tc] = 'O'

        # 확인
        if check():
            return count
        count += 1
        
dir = [[1,0], [-1,0], [0,1], [0,-1]]
# R, C = 1500,1500
# Map = [['X' ]* C for _ in range(R)]
# Map[0][0] = 'L'
# Map[R-1][C-1] = 'L'
R, C = map(int, I().split())
Map = [list(I().strip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
checkVisit = [[False] * C for _ in range(R)]
swany = []
temp = []
for r in range(R):
    for c in range(C):
        if Map[r][c] !='X':
            if Map[r][c] == 'L':
                swany.append((r,c))
            Map[r][c] = 'O'


print(fun())