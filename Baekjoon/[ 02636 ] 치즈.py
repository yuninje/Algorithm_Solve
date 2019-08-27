# https://www.acmicpc.net/problem/2636
import sys
sys.setrecursionlimit(10 ** 6)
I = sys.stdin.readline
def dfs(r,c):
    global queue
    addFlag = False
    for d in dir:
        rr = r+d[0]
        cc = c+d[1]
        if R > rr and rr >= 0 and C > cc and cc >= 0:
            if visit[rr][cc]:
                continue
            if arr[rr][cc] == 1:
                if not addFlag:
                    addFlag = True
                    queue.append([r,c])
            else:
                visit[rr][cc] = True
                dfs(rr,cc)


def bfs():
    global queue
    count = 0
    reset()
    dfs(0,0)
    while queue:
        change = 0
        for q in queue:
            r = q[0]
            c = q[1]
            for d in dir:
                rr = r+d[0]
                cc = c+d[1]
                if R > rr and rr >= 0 and C > cc and cc >= 0 and arr[rr][cc] == 1:
                    change += 1
                    arr[rr][cc] = 0

        reset()
        dfs(0,0)
        count += 1
    return count, change

def reset():
    global queue
    queue = []
    for r in range(0,R):
        for c in range(0,C):
            visit[r][c] = False

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
arr = []
for r in range(0,R):
    arr.append(list(map(int, I().split())))
queue = []
visit = [[False] * C for _ in range(0,R)]
for i in bfs():
    print(i)

