# https://www.acmicpc.net/problem/2567
import sys
sys.setrecursionlimit(10**6)
def dfs(r, c):
    global answer
    for d in dir:
        rr = r + d[0]
        cc = c + d[1]
        if M > rr and rr >= 0 and M > cc and cc >= 0:
            if area[rr][cc] == 0:
                answer += 1
            elif area[rr][cc] == 1 and not visit[rr][cc]:
                visit[rr][cc] = True
                dfs(rr,cc)

M = 110
SIZE = 10
dir = [[1,0], [-1,0], [0,1], [0,-1]]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(0,N)]
area = [[0] * M for _ in range(0,M)]
visit = [[False] * M for _ in range(0,M)]
for a in arr:
    for i in range(a[0]+2, a[0]+SIZE+2):
        for j in range(a[1]+2, a[1]+SIZE+2):
            area[i][j] = 1
answer = 0
for r in range(0,M):
    for c in range(0,M):
        if area[r][c] == 1 and not visit[r][c]:
            visit[r][c] = True
            dfs(r,c) 
for a in area:
    print(a)
print(answer)