def dfs(arr_, red_, blue_, goal, count):
    global answer
    if count >=10:
        return
    
    for d in dir:
        arr = arr_.copy()
        red = red_.copy()
        blue = blue_.copy()
        goalFlag = False
        blue_goalFlag = False
        blueStop = 0
        redStop = 0
        while True:
            # red move
            if arr[red[0]+d[0]][red[1]+d[1]] == 'O' or arr[red[0]+d[0]][red[1]+d[1]] == '.':
                redStop = 0
                arr[red[0]][red[1]] = '.'
                red[0] += d[0]
                red[1] += d[1]
                if arr[red[0]][red[1]] == 'O':
                    goalFlag = True
                else:
                    arr[red[0]][red[1]] = 'R'
            else:
                redStop += 1
            # blue move

            if arr[blue[0]+d[0]][blue[1]+d[1]] == 'O' or arr[blue[0]+d[0]][blue[1]+d[1]] == '.':
                blueStop = 0
                arr[blue[0]][blue[1]] = '.'
                blue[0] += d[0]
                blue[1] += d[1]
                if arr[blue[0]][blue[1]] == 'O':
                    blue_goalFlag = True
                else:
                    arr[blue[0]][blue[1]] = 'B'
            else:
                blueStop += 1

            if blueStop >= 2 and redStop >= 2:
                break
        
        if goalFlag and not blue_goalFlag:
            if answer > count:
                answer = count


        dfs(arr, red, blue, goal, count+1)



N, M = list(map(int, input().split()))

dir = [[1,0],[-1,0],[0,1],[0,-1]]
        # 아래  위에  오른쪽 왼쪽
answer = 11
arr = [[0 for _ in range(0,M)] for __ in range(0,N)]
red = []
blue = []
goal = []
for n in range(0,N):
    line = input()
    for m in range(0,M):
        arr[n][m] = line[m]
        if line[m] == 'R':
            red = [n,m]
        elif line[m] == 'B':
            blue = [n,m]
        elif line[m] == 'O':
            goal = [n,m]

dfs(arr, red, blue, goal, 1)
if answer == 11:
    print(-1)
else:
    print(answer)    

