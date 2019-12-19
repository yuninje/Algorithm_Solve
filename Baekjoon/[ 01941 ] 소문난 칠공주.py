# https://www.acmicpc.net/problem/1941
import sys
sys.setrecursionlimit(10**6)
def dfs(que, total, y, s):
    global answer
    if y + s == 7:
        if s >3:
            answer += 1
        return
    for r, c in que:
        for dr, dc in dir:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < N and 0 <= cc < N and not visit_map[rr][cc]:
                a = 1 << ( rr * N + cc )
                if visit[a + total]:
                    continue
                visit_map[rr][cc] =True
                visit[a + total] = True
                que.append((rr,cc))
                if Map[rr][cc] == 'S':
                    dfs(que, total + a, y, s+1)
                else:
                    dfs(que, total + a, y+1, s)
                del que[-1]
                visit_map[rr][cc] =False

N = 5
Map = [list(input()) for _ in range(N)]
dir = ((1,0), (-1,0), (0,1), (0,-1))
visit_map = [[False] * N for _ in range(N)]
visit = [False] * (1 << ( N * N))
answer = 0
for r in range(N):
    for c in range(N):
        visit_map[r][c] = True
        if Map[r][c] == 'S':
            dfs([(r,c)], 1 << (r * N + c), 0, 1)
        else:
            dfs([(r,c)], 1 << (r * N + c), 1, 0)
        visit_map[r][c] = False

print(answer)