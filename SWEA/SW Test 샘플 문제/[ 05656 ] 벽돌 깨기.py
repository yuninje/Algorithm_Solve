# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
import copy

def dfs(count, arr):
    global MIN
    if count == N:
        total = 0
        for r in range(R):
            for c in range(C):
                if arr[r][c] != 0:
                    total += 1
        MIN = min(MIN, total)
        return

    
    for c in range(0,C):
        arr_ = copy.deepcopy(arr)
        crush(c, arr_)
        down(arr_)
        dfs(count+1, arr_)
        if MIN == 0:
            return

def crush(c, arr):
    r = 0
    while r < R:
        if arr[r][c] != 0:
            break
        r += 1
    if r == R:
        return 0
    visit = [[False] * C for _ in range(R)]
    visit[r][c] = True
    queue = [[r,c]]
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                n = arr[r][c]
                n -= 1
                while R > rr and rr >= 0 and C > cc and cc >= 0 and n > 0 :
                    if not visit[rr][cc]:
                        visit[rr][cc] = True
                        queue_.append([rr,cc])
                    rr += d[0]
                    cc += d[1]
                    n -= 1
            arr[r][c] = 0
        queue = queue_

def down(arr):
    for c in range(C):
        queue = []
        for r in range(R-1, -1, -1):
            if arr[r][c] != 0:
                queue.append(arr[r][c])
                arr[r][c] = 0
        r = R-1
        for q in queue:
            arr[r][c] = q
            r -= 1

dir = [[1,0], [-1,0], [0,1], [0,-1]]
T = int(input())
for test in range(1,T+1):
    N, C, R = list(map(int, input().split()))
    origin = [list(map(int, input().split())) for _ in range(R)]
    total = 0
    MIN = 9999999
    dfs(0,copy.deepcopy(origin))
    print('#' + str(test) + ' ' + str(MIN))
