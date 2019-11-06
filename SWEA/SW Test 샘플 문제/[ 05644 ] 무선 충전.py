# 20 <= TIME <= 100
# 1 <= N <= 8
# BC[n] = C, R, reach, 충전량
# 1 <= BC[N][2] ( 범위 ) <= 4
# 
#     가만히,   상     우     하     좌

def bfs(n):
    global Map
    sc,sr,reach,power = BC[n]
    visit = [[False] * C for _ in range(R)]
    que = [(sr,sc)]
    # print('sr : ' + str(sr) + '  sc : ' + str(sc))
    visit[sr][sc] = True
    while que:
        que_ = []
        for r, c in que:
            Map[r][c][n] = True
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if not (1 <= rr < R and 1 <= cc < C) or abs(rr-sr) + abs(cc-sc) > reach or visit[rr][cc]:
                    continue
                visit[rr][cc] = True
                que_.append((rr,cc))
        que = que_

dir = ((0,0), (-1,0), (0,1), (1,0), (0,-1))
T = int(input())
R, C = 11,11
for test in range(1,T+1):    
    TIME, N = list(map(int, input().split())) 
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(N)]
    BC = sorted(BC, key= lambda x : x[3], reverse=True)

    Map = [[[False] * N for _ in range(C)] for _ in range(R)]
    
    for n in range(N): # BC[n] = C, R, 범위, 충전량
        bfs(n)
    
    time = 0
    ar,ac = 1, 1
    br,bc = R-1, C-1
    answer = 0
    while True:
        add_answer = 0
        an, aan, bn, bbn = -1,-1,-1,-1

        for n in range(N):
            if an != -1 and Map[ar][ac][n]:
                aan = n
                break
            if an == -1 and Map[ar][ac][n]:
                an = n
        
        for n in range(N):
            if bn != -1 and Map[br][bc][n]:
                bbn = n
                break
            if bn == -1 and Map[br][bc][n]:
                bn = n

        if an != -1 and bn != -1:
            if an == bn:
                if aan != -1 and bbn != -1:
                    add_answer = max(BC[an][3] + BC[bbn][3], BC[bn][3] + BC[aan][3])
                elif aan != -1:
                    add_answer = BC[bn][3] + BC[aan][3]
                elif bbn != -1:
                    add_answer = BC[an][3] + BC[bbn][3]
                else:
                    add_answer = BC[an][3]
            else:
                add_answer = BC[an][3] + BC[bn][3]
        elif an != -1: # bn == -1
            add_answer = BC[an][3]
        elif bn != -1:
            add_answer = BC[bn][3]
        else:
            add_answer = 0

        answer += add_answer

        print('time : ' + str(time) + '  answer : ' + str(answer))
        if time == TIME:
            break
        time += 1
        ar += dir[arr[time-1]][0]
        ac += dir[arr[time-1]][1]
        br += dir[brr[time-1]][0]
        bc += dir[brr[time-1]][1]
    print('#' + str(test) + ' ' + str(answer))