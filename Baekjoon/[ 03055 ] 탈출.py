# https://www.acmicpc.net/problem/3055
import sys
I = sys.stdin.readline
def bfs(gosum, water):
    answer = 0

    que = [[gosum[0],gosum[1],0]]
    visit[gosum[0]][gosum[1]] = True
    for wr, wc in water:
        visit[wr][wc] = True
        for dr, dc in dir:
            wwr = wr + dr
            wwc = wc + dc
            if not ( 0 <= wwr < R and 0 <= wwc < C ) or Map[wwr][wwc] == 'D' or Map[wwr][wwc] == 'X':
                continue
            visit[wwr][wwc] = True
            que.append([wwr,wwc,1])
    
    while que:
        que_ = []
        for r, c, v in que:
            if Map[r][c] == 'D':
                return answer
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if not ( 0 <= rr < R and 0 <= cc < C ) or visit[rr][cc] :
                    continue
                if v == 1:
                    if Map[rr][cc] == 'D' or Map[rr][cc] == 'X':
                        continue

                elif v == 0:
                    if Map[rr][cc] == 'X':
                        continue
                
                visit[rr][cc] = True
                que_.append([rr,cc,v])
        que = que_
        answer += 1
    return 'KAKTUS'

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
Map = [list(I()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
gosum = [-1,-1]
water = []
for r in range(R):
    for c in range(C):
        if Map[r][c] == 'S':
            gosum = [r,c]
            Map[r][c] = '.'
        elif Map[r][c] == '*':
            water.append([r,c])
answer = bfs(gosum, water)
print(answer)