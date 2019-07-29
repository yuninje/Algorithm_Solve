# https://www.acmicpc.net/problem/14502
# 0 : 빈칸, 1 : 벽, 2 : 바이러스
#   3 <= N, M <= 8
#   2 <= n(2) <= 10
#   3 <= n(0)

import copy

def spread(arr, r, c):
    if arr[r][c] == 1 or arr[r][c] == 3:
        return
    arr[r][c] = 3
    spread(arr,r+1,c)
    spread(arr,r-1,c)
    spread(arr,r,c+1)
    spread(arr,r,c-1)

def make_wall(wall, r, c, count, string):
    global answer
    if wall[r][c]:
        return
    string += "("+ str(r) + ", " +str(c) + ")  "
    wall[r][c] = True
    arr[r][c] = 1
    count += 1
    if count == 3:
        # 확산
        
        arr_ = copy.deepcopy(arr)
        for n in range(1,N+1):
            for m in range(1,M+1):
                if arr[n][m] == 2:
                    spread(arr_, n, m)
        # 안전지역 갯수
        safe = 0
        for n in range(1,N+1):
            for m in range(1,M+1):
                if arr_[n][m] == 0:
                    safe += 1

        if answer < safe:
            answer = safe
    else:
        for m in range(c+1,M+1):
            make_wall(wall, r, m, count,string)

        for n in range(r+1,N+1):
            for m in range(1, M+1):
                make_wall(wall, n,m, count,string)
    arr[r][c] = 0
    wall[r][c] = False



N, M = list(map(int, input().split()))

arr = [[1 for _ in range(0, M+2)] for __ in range(0, N+2)]
wall = [[True for _ in range(0, M+2)] for __ in range(0, N+2)]
for n in range(1,N+1):
    line = input().split()
    for m in range(1, M+1):
        arr[n][m] = int(line[m-1])
        if arr[n][m] == 0:
            wall[n][m] = False

answer = 0
# 벽으로 막고.
for n in range(1, N+1):
    for m in range(1,M+1):
        if arr[n][m] == 0:
            make_wall(wall,n,m,0, "")
print(answer)