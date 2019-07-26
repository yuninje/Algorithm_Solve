# https://www.acmicpc.net/problem/14499
def left_move(cube):
    temp = cube[3][1]
    cube[3][1] = cube[1][2]
    cube[1][2] = cube[1][1]
    cube[1][1] = cube[1][0]
    cube[1][0] = temp

def right_move(cube):
    temp = cube[3][1]
    cube[3][1] = cube[1][0]
    cube[1][0] = cube[1][1]
    cube[1][1] = cube[1][2]
    cube[1][2] = temp

def up_move(cube):
    temp = cube[3][1]
    cube[3][1] = cube[2][1]
    cube[2][1] = cube[1][1]
    cube[1][1] = cube[0][1]
    cube[0][1] = temp

def down_move(cube):
    temp = cube[0][1]
    cube[0][1] = cube[1][1]
    cube[1][1] = cube[2][1]
    cube[2][1] = cube[3][1]
    cube[3][1] = temp

N, M, r, c, K = list(map(int, input().split()))

cube = [[0 for _ in range(0,3)] for __ in range(0,4)]

area = [[-1 for _ in range(0,M+2)]]
for n in range(0,N):
    area.append([-1] + list(map(int, input().split())) + [-1])
area.append([-1 for _ in range(0,M+2)])
orders = list(map(int, input().split()))

# 1 : 우
# 2 : 좌
# 3 : 위
# 4 : 아래
dir = [[],[0,1], [0,-1], [-1,0],[1,0]]
now = [r+1,c+1]


for o in orders:
    if area[now[0]+dir[o][0]] [now[1]+dir[o][1]] != -1:
        now[0] += dir[o][0]
        now[1] += dir[o][1]
        
        if o == 1:
            right_move(cube)
        elif o == 2:
            left_move(cube)
        elif o == 3:
            up_move(cube)
        elif o == 4:
            down_move(cube)

        if area[now[0]][now[1]] != 0:
            cube[1][1] = area[now[0]][now[1]]
            area[now[0]][now[1]] = 0
        else:
            area[now[0]][now[1]] = cube[1][1]
        print(cube[3][1])