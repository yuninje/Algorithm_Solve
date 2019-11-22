# https://www.acmicpc.net/problem/17836
# 3 <= R, C <= 100
# 1 <= T <= 5000
# 0 : 빈공간
# 1 : 벽
# 2 : 검
import sys
I = sys.stdin.readline
def bfs():
    que = [(0,0)] # r, c, 검
    count = 0
    sword_answer = 999999999
    while que and count <= T and count < sword_answer:
        que_ = []
        for r, c in que:
            if r == R-1 and c == C-1:
                return min(count, sword_answer)
            if Map[r][c] == 2:
                sword_answer = count + (R - 1) - r + (C - 1) - c 
                continue
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not ( 0 <= rr < R and 0 <= cc < C) or visit[rr][cc] or Map[rr][cc] == 1:
                    continue
                que_.append((rr,cc))
                visit[rr][cc] = True                

        que = que_
        count += 1
    if sword_answer <= T:
        return sword_answer
    return 'Fail'

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C, T = list(map(int, I().split()))
Map = [list(map(int, I().split())) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
print(bfs())