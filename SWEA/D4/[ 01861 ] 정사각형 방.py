# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWv0A3daT1QDFAW4&contestProbId=AV5LtJYKDzsDFAXc&probBoxId=AWz_vMZKF1wDFARC&type=PROBLEM&problemBoxTitle=0905_day16&problemBoxCnt=2


dir = [[1,0], [-1,0], [0,1], [0,-1]]
T = int(input())
for test in range(1,T+1):    
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    MAX = 0
    MAX_NUM = -1
    for r in range(N):
        for c in range(N):
            value = 0
            origin_r = r
            origin_c = c
            while True:
                value += 1
                r_ = r
                c_ = c
                for dr, dc in dir:
                    rr = r + dr
                    cc = c + dc
                    if N > rr and rr >= 0 and N > cc and cc >= 0:
                        if Map[r][c] + 1 == Map[rr][cc]:
                            r = rr
                            c = cc
                            break
                if r_ == r and c_ == c:
                    break
            if MAX < value:
                MAX = value
                MAX_NUM = Map[origin_r][origin_c]
            elif MAX == value:
                MAX_NUM = min(MAX_NUM, Map[origin_r][origin_c])


    print('#' + str(test) + ' ' + str(MAX_NUM) + ' ' + str(MAX))