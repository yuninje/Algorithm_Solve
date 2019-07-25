import copy
def dfs( boolList, r, c, total, count):
    global answer
    boolList[r][c] = True
    total += arr[r][c]
    if count == 3:
        if answer < total:
            answer = total
        return
    
    if not boolList[r+1][c]:
        dfs(copy.deepcopy(boolList),r+1, c, total + arr[r+1][c].decode, count+1)
    if not boolList[r-1][c]:  
        dfs(copy.deepcopy(boolList), r-1, c, total + arr[r-1][c], count+1)
    if not boolList[r][c+1]:  
        dfs(copy.deepcopy(boolList), r, c+1, total + arr[r][c+1], count+1)
    if not boolList[r][c-1]:  
        dfs(copy.deepcopy(boolList), r, c-1, total + arr[r][c-1], count+1)


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
        dfs(boolList, r, c, arr[r][c], 0)

print(answer)



