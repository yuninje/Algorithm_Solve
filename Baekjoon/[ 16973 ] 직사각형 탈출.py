# https://www.acmicpc.net/problem/16973
# H, W  는 직사각형 높이 , 가로
# sr, sc 는 시작 r,c
# fr, fc 는 목표 r,c

import sys
from collections import deque
I = sys.stdin.readline

def bfs():
    visit = [[False] * (C+2) for _ in range(R+2)]
    visit[sr][sc] = True
    queue = deque([(sr,sc)])
    count = 0
    while queue:
        len_queue = len(queue)
        count += 1
        print(queue)
        for _ in range(len_queue):
            r, c = queue.popleft()
            for dr, dc in dir1:
                rr = r + dr
                cc = c + dc
                if visit[rr][cc]:
                    continue
                visit[rr][cc] = True
                # 가로만큼 ( W ) 탐색
                for cc in range(c, c+W):
                    if dr == -1:
                        if Map[r-1][cc] == 1:
                            break
                    elif dr == 1:
                        if Map[r+H][cc] == 1:
                            break
                else:
                    queue.append((r+dr,c+dc))
                    if r + dr == fr and c + dc == fc:
                        print(queue)
                        return count

            for dr, dc in dir2: 
                rr = r + dr
                cc = c + dc
                if visit[rr][cc]:
                    continue
                visit[rr][cc] = True
                # 세로만큼 ( H ) 탐색
                for rr in range(r, r+H):
                    if dc == -1:
                        if Map[rr][c-1] == 1:
                            break
                    elif dc == 1:
                        if Map[rr][c+W] == 1:
                            break
                else:
                    queue.append((r+dr,c+dc))
                    if r + dr == fr and c + dc == fc:
                        print(queue)
                        return count
    return -1
dir1 = [[1,0], [-1,0]] # 상 하
dir2 = [[0,1], [0,-1]] # 좌 우


R, C = list(map(int, I().split()))
Map = []
Map.append([1] * (C+2))
for r in range(R):
    Map.append([1]+list(map(int, I().split())) + [1])
Map.append([1] * (C+2))
H,W,sr,sc,fr,fc = list(map(int, I().split()))
print(bfs())