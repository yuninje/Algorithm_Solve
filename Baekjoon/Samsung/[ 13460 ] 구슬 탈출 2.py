# https://www.acmicpc.net/problem/13460
import copy
def dfs(arr, red, blue, goal, count):
    global red_goal
    global blue_goal
    global answer
    if count >=10 or answer <= count:
        return
    
    for d in dir:
        red_goal = False
        blue_goal = False
        arr_ = copy.deepcopy(arr)
        red_ = copy.deepcopy(red)
        blue_ = copy.deepcopy(blue)
        move(arr_, red_, blue_, d)
        if same(arr_, arr):
            continue
        if red_goal and not blue_goal:
            if answer > count+1:
                answer = count+1
        elif blue_goal:
            continue
        else:
            dfs(arr_, red_, blue_, goal, count+1)

def same(arr, arr_):
    for n in range(0,N):
        for m in range(0,M):
            if arr[n][m] != arr_[n][m]:
                return False
    return True

def move(arr, red, blue, d): # 방향  0 : 아래    1 : 위   2 : 오른쪽  3: 왼쪽
    # red move
    global red_goal
    global blue_goal
    while arr[red[0]+d[0]][red[1]+d[1]] == 'O' or arr[red[0]+d[0]][red[1]+d[1]] == '.':
        arr[red[0]][red[1]] = '.'
        red[0] += d[0]
        red[1] += d[1]
        if arr[red[0]][red[1]] == 'O':
            red_goal = True
            break
        else:
            arr[red[0]][red[1]] = 'R'
    
    # blue move
    while arr[blue[0]+d[0]][blue[1]+d[1]] == 'O' or arr[blue[0]+d[0]][blue[1]+d[1]] == '.':
        arr[blue[0]][blue[1]] = '.'
        blue[0] += d[0]
        blue[1] += d[1]
        if arr[blue[0]][blue[1]] == 'O':
            blue_goal = True
            break
        else:
            arr[blue[0]][blue[1]] = 'B'
    #red move
    if not red_goal :
        while arr[red[0]+d[0]][red[1]+d[1]] == 'O' or arr[red[0]+d[0]][red[1]+d[1]] == '.':
            arr[red[0]][red[1]] = '.'
            red[0] += d[0]
            red[1] += d[1]
            if arr[red[0]][red[1]] == 'O':
                red_goal = True
                break
            else:
                arr[red[0]][red[1]] = 'R'





N, M = list(map(int, input().split()))

dir = [[1,0],[-1,0],[0,1],[0,-1]]
        # 아래  위에  오른쪽 왼쪽

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


red_goal = False
blue_goal = False
answer = 11
dfs(arr, red, blue, goal, 0)
if answer == 11:
    print(-1)
else :
    print(answer)
