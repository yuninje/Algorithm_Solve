# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWv0A3daT1QDFAW4&contestProbId=AV15OZ4qAPICFAYD&probBoxId=AWyzMqVathYDFAVP&type=PROBLEM&problemBoxTitle=0821_day11_ws&problemBoxCnt=1

def dfs(now, count, total):
    global MIN
    if count == N:
        total += inner[now][1]
        MIN = min(MIN, total)
        return

    if MIN < total:
        return

    for i in range(2,N+2):
        if visit[i]:
            continue
        visit[i] = True
        dfs(i, count+1, total + inner[now][i])
        visit[i] = False


T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr_ = list(map(int, input().split()))
    arr = []
    for n in range(0,N+2):
        arr.append([arr_[2*n], arr_[2*n+1]])
    visit = [False] * (N+2)
    inner = [[0] * (N+2) for _ in range(0,N+2)]
    MIN = 999999999
    for i in range(0,N+2):
        for j in range(i+1,N+2):
            inner[i][j] = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) 
            inner[j][i] = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) 
    
    dfs(0, 0,0)
    print("#" + str(test) + " " + str(MIN))