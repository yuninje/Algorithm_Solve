# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWv0A3daT1QDFAW4&contestProbId=AV5LyE7KD2ADFAXc&probBoxId=AWz_vMZKF1wDFARC&type=PROBLEM&problemBoxTitle=0905_day16&problemBoxCnt=2
# . : 평지
# * : 벽돌
# # : 강철
# - : 물 ( 전차 X)
# ^ : 
# v
# <
# >

def shoot():
    r, c, d = now
    rr = r + dir[d][0]
    cc = c + dir[d][1]

    while R > rr and rr >= 0 and C > cc and cc >= 0:
        if Map[rr][cc] == '*': # 벽돌벽
            Map[rr][cc] = '.'
            break
        elif Map[rr][cc] == '#': # 강철벽
            break
        rr += dir[d][0]
        cc += dir[d][1]

def turn(num):
    now[2] = num
    r, c, d = now
    rr = r + dir[d][0]
    cc = c + dir[d][1]
    if R > rr and rr >= 0 and C > cc and cc >= 0:
        if Map[rr][cc] == '.':
            now[0] = rr
            now[1] = cc

#        상      우     하      좌
dir = [[-1,0], [0,1], [1,0], [0,-1]]
T = int(input())
for test in range(1, T+1):
    R, C = list(map(int, input().split()))
    Map = [list(input()) for _ in range(R)]
    N = int(input())
    order = input()
    now = 0
    for r in range(R):
        for c in range(C):
            if Map[r][c] == '^':
                now = [r,c,0]
            elif Map[r][c] == '>':
                now = [r,c,1]
            elif Map[r][c] == 'v':
                now = [r,c,2]
            elif Map[r][c] == '<':
                now = [r,c,3]
    Map[now[0]][now[1]] = '.'

    for o in order:
        if o == 'S':
            shoot()
        elif o == 'U':
            turn(0)
        elif o == 'R':
            turn(1)
        elif o == 'D':
            turn(2)
        elif o == 'L':
            turn(3)
    
    r,c,d = now
    if d == 0:
        Map[r][c] = '^'
    elif d == 1:
        Map[r][c] = '>'
    elif d == 2:
        Map[r][c] = 'v'
    elif d == 3:
        Map[r][c] = '<'

    print('#' + str(test), end=' ')
    for m in Map:
        print(''.join(m))
    print()




