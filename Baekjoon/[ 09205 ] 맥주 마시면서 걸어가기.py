# https://www.acmicpc.net/problem/9205
import sys
I = sys.stdin.readline
def dfs(nowR, nowC):
    global happyFlag
    if happyFlag:
        return
    if abs(nowR -rock[0]) + abs(nowC-rock[1]) <= 1000:
        happyFlag = True
        return
    for d in range(0,de):
        if abs(nowR + - deList[d][0])+ abs(nowC -deList[d][1]) <= 1000 and not visit[d]:
            visit[d] = True
            dfs(deList[d][0], deList[d][1])


test = int(I())
for t in range(0,test):
    de = int(I())
    home = list(map(int,I().split()))
    deList = []
    for d in range(0,de):
        deList.append(list(map(int,I().split())))
    rock = list(map(int,I().split()))

    visit = [False] * de
    happyFlag = False

    dfs(home[0], home[1])

    if happyFlag:
        print('happy')
    else:
        print('sad')
