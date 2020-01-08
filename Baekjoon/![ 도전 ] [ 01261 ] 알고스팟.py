# https://www.acmicpc.net/problem/1261
# 1 <= N, M <= 100
from queue import PriorityQueue
import sys
I = sys.stdin.readline

def bfs():
    que = PriorityQueue()
    que.put((0,0,0))
    
    while not que.empty():
        v, r, c = que.get()
        if r == R-1 and c == C-1:
            return v
        for dr, dc in dir:
            rr, cc = r + dr, c + dc
            if not (0 <= rr < R and 0 <= cc < C):
                continue
            vv = v+1 if Map[rr][cc]=='1' else v
            if vv == RC or visit[vv][rr][cc]:
                continue
            visit[vv][rr][cc] = True
            que.put((vv,rr,cc))
    

C,R = map(int, I().split())
Map = [list(input()) for _ in range(R)]
dir = [[1,0],[0,1],[-1,0],[0,-1]]
RC = R + C - 1
visit = [[[False] * C for _ in range(R)]  for _ in range(RC)]
print(bfs())