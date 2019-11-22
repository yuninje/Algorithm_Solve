# R : Map 세로 크기         5 <= R <= 50
# C : Map 가로 크기         5 <= C <= 50
# HOLE_R : HOLE 의 세로     
# HOLE_C : HOLE 의 가로
# L : 탈출 후 소요된 시간   1 <= L <= 20
def bfs(r,c):
    que = [(r,c)]
    visit[r][c] = True
    time = 0
    count = 0
    while que and time < L:
        que_ = []

        for r, c in que:
            count += 1
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                gor,goc = r + 2 * dr, c + 2 * dc
                if not(0 <= gor < RR and 0 <= goc < CC) or visit[gor][goc]:
                    continue
                
                if Map[rr][cc] == 2:
                    que_.append((gor,goc))
                    visit[gor][goc] = True

        que = que_
        time += 1

    return count


dir = [[1,0],[-1,0],[0,1],[0,-1]]
T = int(input())
for test in range(1,T+1):
    R, C, OHOLE_R, OHOLE_C, L = list(map(int, input().split()))
    OMap = [list(map(int, input().split())) for _ in range(R)]
    RR, CC = R * 2 + 1, C * 2 + 1
    Map = [[0] * (CC) for _ in range(RR)]
    visit = [[False] * (CC) for _ in range(RR)]
    for r in range(R):
        rr = r * 2 + 1
        for c in range(C):
            cc = c * 2 + 1
            Map[ rr ][ cc ] = OMap[r][c]
            if OMap[r][c] == 1:
                Map[ rr -1 ][ cc ] += 1 # UP
                Map[ rr + 1 ][ cc ] += 1 # DOWN
                Map[ rr ][ cc - 1 ] += 1 # LEFT
                Map[ rr ][ cc + 1 ] += 1 # RIGHT
            elif OMap[r][c] == 2:
                Map[ rr -1 ][ cc ] += 1 # UP
                Map[ rr + 1  ][ cc ] += 1 # DOWN
            elif OMap[r][c] == 3:
                Map[ rr ][ cc - 1 ] += 1 # LEFT
                Map[ rr ][ cc + 1 ] += 1 # RIGHT
            elif OMap[r][c] == 4:
                Map[ rr -1 ][ cc ] += 1 # UP
                Map[ rr ][ cc + 1 ] += 1 # RIGHT
            elif OMap[r][c] == 5:
                Map[ rr + 1  ][ cc ] += 1 # DOWN
                Map[ rr ][ cc + 1 ] += 1 # RIGHT
            elif OMap[r][c] == 6:
                Map[ rr + 1  ][ cc ] += 1 # DOWN
                Map[ rr ][ cc - 1 ] += 1 # LEFT
            elif OMap[r][c] == 7:
                Map[ rr -1 ][ cc ] += 1 # UP
                Map[ rr ][ cc - 1 ] += 1 # LEFT

    hole_r = 2 * OHOLE_R + 1
    hole_c = 2 * OHOLE_C + 1
    
    answer = bfs(hole_r,hole_c)

    print('#' + str(test) + ' ' + str(answer))