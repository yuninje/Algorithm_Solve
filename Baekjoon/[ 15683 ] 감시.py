# https://www.acmicpc.net/problem/15683
# 1 <= N , M <= 8
# 0 : 빈칸  , 6 : 벽
# 1 : 한방향, 2 : 양방향,  3: 90도 , 4 : 2+3 , 5 : 전방향
# cctv <= 8
def dfs(arr, now, dir_list, change):
    global answer
    change_list = []
    for d in dir_list:
        r = cctv[now][1]
        c = cctv[now][2]
        while True:
            if arr[r + dir[d][0]][c + dir[d][1]] == 6:
                break
            elif arr[r + dir[d][0]][c + dir[d][1]] == 0:
                arr[r + dir[d][0]][c + dir[d][1]] = 7
                change_list.append([r + dir[d][0],c + dir[d][1]])
                change+= 1
            r += dir[d][0]
            c += dir[d][1]

    now += 1    
    if now == len(cctv):
        if answer > count0 - change:
            answer = count0 - change
        for c in change_list:
            arr[c[0]][c[1]] = 0
        return

    if cctv[now][0] == 1:
        dfs(arr, now, [0], change)
        dfs(arr, now, [1], change)
        dfs(arr, now, [2], change)
        dfs(arr, now, [3], change)
    elif cctv[now][0] == 2:
        dfs(arr, now, [0,2], change)
        dfs(arr, now, [1,3], change)
    elif cctv[now][0] == 3:
        dfs(arr, now, [0,1], change)
        dfs(arr, now, [1,2], change)
        dfs(arr, now, [2,3], change)
        dfs(arr, now, [3,0], change)    
    elif cctv[now][0] == 4:
        dfs(arr, now, [0,1,2], change)
        dfs(arr, now, [1,2,3], change)
        dfs(arr, now, [2,3,0], change)
        dfs(arr, now, [3,0,1], change)
    else:
        dfs(arr, now, [0,1,2,3], change)

    for c in change_list:
        arr[c[0]][c[1]] = 0


N, M = list(map(int, input().split()))
arr=[[6] * (M+2) for _ in range(0,N+2)]
cctv = []
count0 = 0
for n in range(1,N+1):
    line = input().split()
    for m in range(1,M+1):
        arr[n][m] = int(line[m-1])
        if arr[n][m] == 0:
            count0 += 1
        if arr[n][m] != 0 and arr[n][m] != 6:
            cctv.append([arr[n][m],n,m])
# 0 : 동, 1 : 남 , 2 : 서 , 3 : 북
dir = [[0,1], [1,0], [0,-1], [-1,0]]

answer = count0

dfs(arr, -1, [],0)
print(answer)