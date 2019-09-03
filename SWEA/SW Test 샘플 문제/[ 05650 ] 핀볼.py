# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo

def simulation(r,c,d):
    global MAX
    # 전진
    count = 0
    rr = r + d[0]
    cc = c + d[1]
    dd = d
    while True:
        # 벽을 만남.
        if rr >= N or rr < 0 or cc >= N or cc < 0:
            dd = [dd[0] * (-1), dd[1] * (-1)]
            count += 1
        elif area[rr][cc] == 0:
            pass
        elif area[rr][cc] == -1 or area[rr][cc] == -2:
            break
        elif area[rr][cc] == 1:
            if dd == [-1,0]: # 상 -> 하
                dd = [1,0] 
            elif dd == [1,0]: # 하 -> 우
                dd = [0,1]
            elif dd == [0,-1]: # 좌 -> 상
                dd = [-1,0]
            elif dd == [0,1]: # 우 -> 좌
                dd = [0,-1]
            count += 1
        elif area[rr][cc] == 2:
            if dd == [-1,0]: # 상 -> 우
                dd = [0,1]
            elif dd == [1,0]: # 하 -> 상
                dd = [-1,0]
            elif dd == [0,-1]: # 좌 -> 하
                dd = [1,0]
            elif dd == [0,1]: # 우 -> 좌
                dd = [0,-1]
            count += 1
        elif area[rr][cc] == 3:
            if dd == [-1,0]: # 상 -> 좌
                dd = [0,-1]
            elif dd == [1,0]: # 하 -> 상
                dd = [-1,0]
            elif dd == [0,-1]: # 좌 -> 우
                dd = [0,1]
            elif dd == [0,1]: # 우 -> 하
                dd = [1,0]
            count += 1
        elif area[rr][cc] == 4:
            if dd == [-1,0]: # 상 -> 하
                dd = [1,0]
            elif dd == [1,0]: # 하 -> 좌
                dd = [0,-1]
            elif dd == [0,-1]: # 좌 -> 우
                dd = [0,1]
            elif dd == [0,1]: # 우 -> 상
                dd = [-1,0]
            count += 1
        elif area[rr][cc] == 5:
            dd = [dd[0] * (-1) , dd[1] * (-1)]
            count += 1
        else:
            breakFlag = False
            for rrr in range(0,N):
                for ccc in range(0,N):
                    if area[rrr][ccc] == area[rr][cc] and (rrr != rr or ccc != cc):
                        rr = rrr
                        cc = ccc
                        breakFlag = True
                        break
                if breakFlag:
                    break
        rr += dd[0]
        cc += dd[1]
    MAX = max(MAX, count)

dir = [[1,0], [0,1], [-1,0], [0,-1]]
T = int(input())
for test in range(1,T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    # 0인 모든 지역에서 4가지 방향으로 시작.
    for r in range(0,N):
        for c in range(0,N):
            if area[r][c] == 0:
                area[r][c] = -2
                for d in dir:
                    simulation(r,c,d)
                area[r][c] = 0
    print('#' + str(test) + ' ' + str(MAX))