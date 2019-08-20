# https://www.acmicpc.net/problem/2146
# 1 <= N <= 100
# 0 : 바다, 1 : 육지
import sys
sys.setrecursionlimit(10**6)
def dfs(r, c):
    global queue
    for d in dir:
        rr = r+d[0]
        cc = c+d[1]
        if N > rr and rr >= 0 and N > cc and cc >= 0 and arr[rr][cc] == 1 and not visit[rr][cc]:
            visit[rr][cc] = True
            dfs(rr, cc)
            queue.append([rr, cc])
    
def bfs(queue):
    global MIN
    count = 0
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]

            for d in dir:
                rr = r+d[0]
                cc = c+d[1]
                if N > rr and rr >= 0 and N > cc and cc >= 0 and not visit[rr][cc]:
                    if arr[rr][cc] == 0:
                        visit[rr][cc] = True
                        queue_.append([rr,cc])
                    else:
                        MIN = min(MIN, count)
        queue = queue_
        count += 1
        if count > MIN:
            return

def reset():
    for r in range(0,N):
        for c in range(0,N):
            if arr[r][c] == 0:
                visit[r][c] = False


dir = [[1,0], [-1,0], [0,1], [0,-1]]
N = int(input())
arr = []
for n in range (0,N):
    arr.append(list(map(int,input().split())))
visit = [[False] * N for _ in range(0,N)]

MIN = 9999
for r in range(0,N):
    for c in range(0,N):
        if arr[r][c] == 1 and not visit[r][c]:
            queue = [[r,c]]
            visit[r][c] = True
            dfs(r,c)
            bfs(queue)
            reset()
print(MIN)
