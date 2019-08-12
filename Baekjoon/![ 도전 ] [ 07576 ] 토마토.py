# https://www.acmicpc.net/problem/7576
# 2 <= M, N <= 1000
# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토 X
import sys
sys.setrecursionlimit(10**6)    # Maximum Recursion Dept Exceed

I = sys.stdin.readline
def bfs():
    global q
    day = 0
    count = len(q)
    while q:
        if count == 0:
            count = len(q)
            print(q)
            if check():
                return day
            day += 1

        now = q[0]
        del q[0]

        if arr[now[0]][now[1]] != 0 and day != 0:
            count -= 1
            continue
        if visit[now[0]][now[1]]:
            count -= 1
            continue

        arr[now[0]][now[1]] = 1 
        visit[now[0]][now[1]] = True

        
        for d in dir:
            q.append([now[0] + d[0],now[1] + d[1]])
        count -= 1
    if check():
        return day
    return -1


def check():
    for r in range(1,N+1):
        for c in range(1,M+1):
            if arr[r][c] == 0:
                return False
    return True

M, N = list(map(int, I().split()))

dir = [[1,0],[-1,-0],[0,1],[0,-1]]
q = []
visit = [[False] * (M+2) for _ in range(0,N+2)]
arr = []
arr.append([-1]*(M+2))
for r in range(1,N+1):
    arr.append([-1]+list(map(int, I().split()))+[-1])
    for c in range(1,M+1):
        if arr[r][c] == 1:
            q.append([r,c])

arr.append([-1]*(M+2))
day = 0
for r in range(1,N+1):
    for c in range(1,M+1):
        if arr[r][c] == 0:
            for d in dir:
                if arr[r+d[0]][c+d[1]] != 1:
                    break
            else:
                day = -1
if day == -1:
    print(day)
else:
    if check():
        print(0)
    else:
        print(bfs())