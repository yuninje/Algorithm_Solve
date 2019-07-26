# https://www.acmicpc.net/problem/14500
import copy

def dfs( boolList, r, c, total, count):
    global answer

    if boolList[r][c]:
        return
    boolList[r][c] = True
    total += arr[r][c]
    if count == 3:
        if answer < total:
            answer = total
        return
    

    if count == 2 and boolList[r-1][c] and boolList[r-2][c] and r-2>0:
        dfs(copy.deepcopy(boolList),r-1, c+1, total , count+1)
        dfs(copy.deepcopy(boolList),r-1, c-1, total , count+1)

    if count == 2 and boolList[r][c-1] and boolList[r][c-2] and c-2 >0:
        dfs(copy.deepcopy(boolList),r+1, c-1, total , count+1)
        dfs(copy.deepcopy(boolList),r-1, c-1, total , count+1)

    dfs(copy.deepcopy(boolList),r+1, c, total , count+1)
    #dfs(copy.deepcopy(boolList), r-1, c, total, count+1)
    dfs(copy.deepcopy(boolList), r, c+1, total, count+1)
    dfs(copy.deepcopy(boolList), r, c-1, total, count+1)


# 4 <= N, M <= 500
N, M = list(map(int, input().split()))

arr = [[0 for _ in range(0,M+2)] for _ in range(0,N+2)]

for r in range(1,N+1):
    line = input().split()
    for c in range(1,M+1):
        arr[r][c] = int(line[c-1])

boolList = [[False for _ in range(0,M+2)] for _ in range(0,N+2)]
for i in range(0,N+2):
    boolList[i][0] = True
    boolList[i][M+1] = True
for i in range(0,M+2):
    boolList[0][i] = True
    boolList[N+1][i] = True

answer = 0
for r in range(1,N+1):
    for c in range(1,M+1):
        dfs(copy.deepcopy(boolList), r, c, 0, 0)
print(answer)