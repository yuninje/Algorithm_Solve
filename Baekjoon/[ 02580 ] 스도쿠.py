# https://www.acmicpc.net/problem/2580

def dfs(count):
    global answerFlag
    count += 1

    if count == len0_len:
        answerFlag = True
        return

    nowR = list0[count][0]
    nowC = list0[count][1]

    no_list = [True] * 9
    # 속한 세로
    for r in range(0,9):
        if arr [r] [nowC] != 0 :
            no_list[arr [r] [nowC] -1] = False

    # 속한 가로
    for c in range(0,9):
        if arr [nowR] [c] != 0 :
            no_list[arr [nowR] [c] -1] = False
    
    # 속한 사각형
    for r in range(nowR//3 *3, nowR // 3 * 3 + 3):
        for c in range(nowC//3 *3, nowC//3 * 3 + 3):
            if arr[r][c] != 0:
                no_list[arr[r][c]-1] = False

    for n in range(0,9):
        if no_list[n]:
            arr[nowR][nowC] = n+1
            dfs(count)
        if answerFlag:
            return

    arr[nowR][nowC] = 0


arr = []
list0 = []
for r in range(0,9):
    arr.append(list(map(int, input().split())))
    for c in range(0,9):
        if arr[r][c] == 0:
            list0.append([r,c])
len0_len = len(list0)
answerFlag = False
dfs(-1)

for line in arr:
    print(" ".join(map(str, line)))