# https://www.acmicpc.net/problem/2933
# . : 빈칸, x : 미네랄
# 1 <= R , C <= 100
# 1 <= N <= 100
def crush(h, d):
    rr = R - h
    cc = pos[d]
    dc = dir[d][1]
    
    while rr >= 0 and rr < R and cc >= 0 and cc < C:
        if Map[rr][cc] == 'x':
            Map[rr][cc] = '.'
            break
    
        cc += dc 

def check():
    for r in range(R):
        for c in range(C):
            visit[r][c] = False
    for r in range(R):
        for c in range(C):
            if Map[r][c] == 'x':
                if visit[r][c]:
                    continue
                bfs(r,c)

def bfs(r,c):
    que = [[r,c]]
    group = [[r,c]]
    flag = False
    while que:
        que_ = []
        for r, c in que:
            if r == R-1:
                flag = True

            for dr, dc in dir:
                rr = r + dr
                cc = c + dc

                if 0 <= rr and rr < R and 0 <= cc  and cc < C and not visit[rr][cc] and Map[rr][cc] == 'x':
                    que_.append([rr,cc])
                    visit[rr][cc] = True
        que = que_
        group += que_

    if not flag:
        down(group)

def down(group):
    flag = True

    for r, c in group:
        Map[r][c] = '.'
    while flag:
        for r, c in group:
            if r+1 < R:
                if Map[r+1][c] == 'x':
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            for i in range(len(group)):
                group[i][0] += 1

    for r, c in group:
        Map[r][c] = 'x'
        visit[r][c] = True

R, C = list(map(int, input().split()))
Map = [list(input()) for _ in range(R)]
N = int(input())
arr = list(map(int, input().split()))
visit = [[False] * C for _ in range(R)]
dir = [[0,1], [0,-1], [1,0], [-1,0]]
pos = [0,C-1]

for i in range(len(arr)):
    # break
    crush(arr[i], i%2)
    # down
    check()

for m in Map:
    print(''.join(m))