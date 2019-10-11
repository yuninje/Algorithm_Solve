# https://www.acmicpc.net/problem/9376
# . : 빈공간
# * : 벽
# # : 문
# $ : 죄수
import sys
sys.setrecursionlimit(10**6)
def dfs(r,c,count,flag, visit):
    global answer
    if count > answer :
        return
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc

        # 탐색
        if 0 <= rr and rr < R and 0 <= cc and cc < C:
            if visit[rr][cc]:
                continue

            visit[rr][cc] = True

            if Map[rr][cc] == '*':
                continue

            elif Map[rr][cc] == '.':
                dfs(rr,cc,count,flag, visit)

            elif Map[rr][cc] == '#':
                Map[rr][cc] = '.'
                dfs(rr,cc,count+1,flag, visit)
                Map[rr][cc] = '#'

            elif Map[rr][cc] == '$':
                if flag:
                    answer = min(answer, count)
                else:
                    visit_ = [[False] * C for _ in range(R)]
                    visit_[rr][cc] = True
                    dfs(rr,cc,count,True, visit_)
            visit[rr][cc] = False

dir = [[1,0], [-1,0], [0,1], [0,-1]]
T = int(input())
for test in range(1,T+1):
    R, C = list(map(int, input().split()))
    Map = [list(input()) for _ in range(R)]
    
    for m in Map:
        print(m)
    
    # 시작 지점 찾기
    answer = 999999999
    visit = [[False] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                if Map[r][c] == '*':
                    continue
                else:
                    visit[r][c] = True
                    if Map[r][c] == '.':
                        dfs(r,c,0,False, visit)
                    elif Map[r][c] == '#':
                        dfs(r,c,1,False, visit)
                    elif Map[r][c] == '$':
                        dfs(r,c,0,True, visit)
                    visit[r][c] = False
    #  dfs 탐색
    print(answer)
