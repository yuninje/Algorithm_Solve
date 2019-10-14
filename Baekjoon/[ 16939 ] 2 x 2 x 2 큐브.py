#  https://www.acmicpc.net/problem/16939


def turn_sero():
    # [0,2] ~ [5,2]
    temp0 = Map[0][2]
    temp1 = Map[1][2]
    for r in range(4):
        Map[r][2] = Map[r+2][2]
    Map[4][2] = Map[3][7]
    Map[5][2] = Map[2][7]
    Map[3][7] = temp0
    Map[2][7] = temp1

    # [2,0] ~ [3,1]
    temp = Map[2][0]
    Map[2][0] = Map[2][1]
    Map[2][1] = Map[3][1]
    Map[3][1] = Map[3][0]
    Map[3][0] = temp

def turn_garo():
    # [3,0] ~ [3,8]
    temp0 = Map[2][0]
    temp1 = Map[2][1]
    for c in range(6):
        Map[2][c] = Map[2][c+2]
    Map[2][6] = temp0
    Map[2][7] = temp1

    # [0,2] ~ [1,3]
    temp = Map[0][2]
    Map[0][2] = Map[1][2]
    Map[1][2] = Map[1][3]
    Map[1][3] = Map[0][3]
    Map[0][3] = temp

def turn_aa():
    temp0 = Map[2][0]
    temp1 = Map[3][0]
    Map[2][0] = Map[0][3]
    Map[3][0] = Map[0][2]
    Map[0][3] = Map[3][5]
    Map[0][2] = Map[2][5]
    Map[3][5] = Map[5][2]
    Map[2][5] = Map[5][3]
    Map[5][2] = temp0
    Map[5][3] = temp1

    temp = Map[3][6]
    Map[3][6] = Map[3][7]
    Map[3][7] = Map[2][7]
    Map[2][7] = Map[2][6]
    Map[2][6] = temp



def check():
    for r, c in list_:
        num = Map[r][c]
        for rr in range(r,r+2):
            for cc in range(c, c+2):
                if Map[rr][cc] != num:
                    return False

    return True

str_ = input().split()
Map = [[0] * 8 for _ in range(6)]
list_ = [[0,2], [2,2], [4,2], [2,0], [2,4], [2,6]]
idx = 0
for r, c in list_:
    for rr in range(r, r+2):
        for cc in range(c, c+2):
            Map[rr][cc] = int(str_[idx])
            idx += 1
answer = 0

for i in range(4):
    turn_garo()
    if i == 0 or i == 2:
        if check():
            answer = 1
for i in range(4):
    turn_sero()
    if i == 0 or i == 2:
        if check():
            answer = 1
for i in range(4):
    turn_aa()
    if i == 0 or i == 2:
        if check():
            answer = 1
print(answer)