# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE

def dfs(nowR,nowC):
    global result
    if nowR == N-1:
        result += 1
        return

    for c in range(0,N):
        if arr[nowR+1][c] == 0:
            check_area(nowR+1, c)
            arr[nowR+1][c] = -1
            dfs(nowR+1,c)
            uncheck_area(nowR+1, c)


def check_area(nowR,nowC):
    for r in range(0,N):
        if arr[r][nowC] == 0:
            arr[r][nowC] = nowR+1
    for c in range(0,N):
        if arr[nowR][c] == 0:
            arr[nowR][c] = nowR+1
    for n in range(1,N):
        for d in dir:
            r = nowR + d[0] * n
            c = nowC + d[1] * n
            if N > r and r >= 0 and N > c and c >= 0:
                if arr[r][c] == 0:
                    arr[r][c] = nowR+1
        


def uncheck_area(nowR, nowC):
    for r in range(0,N):
        for c in range(0,N):
            if arr[r][c] == nowR+1:
                arr[r][c] = 0
    arr[nowR][nowC] = 0

dir = [[-1,-1], [1,1], [-1,1], [1,-1]]
T = int(input())
for test in range(1,T+1):
    N = int(input())
    result = 0

    arr = [[0] * N for _ in range(0,N)]
    dfs(-1,-1)
    print('#'+str(test) + ' ' + str(result))