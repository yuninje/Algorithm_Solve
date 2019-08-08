# https://www.acmicpc.net/problem/9205
def dfs(nowR, nowC):
    global happyFlag
    global visit
    # print("nowR : " + str(nowR) + "  nowC : " + str(nowC))
    if happyFlag:
        return
    if abs(nowR -rock[0]) + abs(nowC-rock[1]) <= 1000:
        happyFlag = True
        return
    for d in range(0,de):
        if abs(nowR + - deList[d][0])+ abs(nowC -deList[d][1]) <= 1000 and not visit[d]:
            visit[d] = True
            dfs(deList[d][0], deList[d][1])


test = int(input())
for t in range(0,test):
    de = int(input())
    home = list(map(int,input().split()))
    deList = []
    for d in range(0,de):
        deList.append(list(map(int,input().split())))
    rock = list(map(int,input().split()))

    visit = [False] * de
    happyFlag = False

    dfs(home[0], home[1])

    if happyFlag:
        print('happy')
    else:
        print('sad')
