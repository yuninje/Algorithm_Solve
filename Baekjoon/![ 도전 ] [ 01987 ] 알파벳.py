# https://www.acmicpc.net/problem/1987
# 1 <= R, C <= 20

def dfs(r,c, count):
    global answer

    if answer < count:
        answer = count
    
    for dr, dc in dir:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C and not visit[ord(Map[rr][cc])-ord('A')] and not visit_Map[rr][cc]:
            visit_Map[rr][cc] = True
            visit[ord(Map[rr][cc])-ord('A')] = True
            dfs(rr,cc,count+1)
            visit[ord(Map[rr][cc])-ord('A')] = False
            visit_Map[rr][cc] = False

R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
visit_Map = [[False] * C  for _ in range(R)] 
visit = [False] * 26
dir = [[0,1], [0,-1], [1,0], [-1,0]]
visit[ord(Map[0][0]) - ord('A')] = True
visit_Map[0][0] = True
answer = 0
dfs(0,0,1)
print(answer)