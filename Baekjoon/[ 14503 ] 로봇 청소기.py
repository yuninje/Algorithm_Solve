# https://www.acmicpc.net/problem/14503
# N * M
# 0 : 청소X  1 : 벽   2 : 청소O
# 0 : 북  , 1 : 동  , 2 : 남, 3 : 서

N, M = list(map(int, input().split()))
nowR, nowC, nowD = list(map(int, input().split()))
nowR += 1
nowC += 1
arr = [[1 for _ in range(0,M+2)] for __ in range(0,N+2)]
for n in range(1,N+1):
    line = input().split()
    for m in range(1,M+1):
        arr[n][m] = int(line[m-1])

dir = [[-1,0], [0,1], [1,0], [0,-1]]

answer = 0
while True:
    # 청소
    if arr[nowR][nowC] == 0:
        answer += 1
    arr[nowR][nowC] = 2
    # 현재 방향 기준 왼쪽방향부터 탐색
    turnCount = 0
    while turnCount < 4:
        nowD -= 1
        nowD %= 4
        if arr[nowR + dir[nowD][0]][nowC + dir[nowD][1]] == 0:
            break
        turnCount += 1
    if turnCount == 4:
        if arr[nowR + dir[(nowD+2)%4][0]][nowC + dir[(nowD+2)%4][1]] == 1:
            break
        else:
            nowR += dir[(nowD+2)%4][0]
            nowC += dir[(nowD+2)%4][1]
    else:
        # 청소 안되어있음
        nowR += dir[nowD][0]
        nowC += dir[nowD][1]

print(answer)