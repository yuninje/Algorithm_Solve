# https://www.acmicpc.net/problem/1726

def dfs(nowR, nowC, d, order, turnFlag):
    global answer
    if visit[nowR][nowC] and not turnFlag:
        print("nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d) +  "  order : " + str(order) + " 이미 방문함 " )
        return
    if area[nowR][nowC] == 1:
        print("nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d) +  "  order : " + str(order) +  " 벽임 " )
        return
    if order > answer:
        print("nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d) +  "  order : " + str(order) + " 횟수가 너무 많음" )
        return
    
    if dp[nowR][nowC] > order:
        dp[nowR][nowC] = order+1
    elif turnFlag:
        pass
    else:
        print("nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d) +  "  order : " + str(order) + " 더 효율적인 곳이 있음 " )
        return

    if nowR == end[0] and nowC == end[1] :
        if end[2] == d:
            answer = min(answer, order)
        else:
            answer = min(answer, order+1)
        print("===================도착 !!  " + "    nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d) +  "  answer : " + str(answer))
        return

    visit[nowR][nowC] = True

    print("nowR : " + str(nowR) + "   nowC : " + str(nowC) + "  d : " + str(d)  +  "  order : " + str(order))

    if area[nowR + dir[d][0] * 1][nowC + dir[d][1] * 1] == 0:
        dfs(nowR + dir[d][0] * 1, nowC + dir[d][1] * 1, d, order+1, False)     # 고대로 전진 1
        if area[nowR + dir[d][0] * 2][nowC + dir[d][1] * 2] == 0:
            dfs(nowR + dir[d][0] * 2, nowC + dir[d][1] * 2, d, order+1, False)     # 고대로 전진 2
            if area[nowR + dir[d][0] * 3][nowC + dir[d][1] * 3] == 0:
                dfs(nowR + dir[d][0] * 3, nowC + dir[d][1] * 3, d, order+1, False)     # 고대로 전진 3
                
    if (d == 1 or d == 2) and not turnFlag:                                            
        dfs(nowR, nowC, 3, order+1, True)                                 # 남으로 턴
        dfs(nowR, nowC, 4, order+1, True)                                 # 북으로 턴
    elif (d == 3 or d == 4) and not turnFlag:
        dfs(nowR, nowC, 1, order+1, True)                                 # 동으로 턴
        dfs(nowR, nowC, 2, order+1, True)                                 # 서로 턴
    
    visit[nowR][nowC] = False

dir = [[],[0,1], [0,-1],[1,0], [-1,0]]  # 1 : 동, 2 : 서, 3 : 남, 4 : 북
R,C = list(map(int,input().split()))
area = [[1] * (C+6) for _ in range(0,R+6)]
for r in range(3,R+3):
    line = input().split()
    for c in range(3, C+3):
        area[r][c] = int(line[c-3])

start = list(map(lambda x : int(x)+2, input().split()))
start[2] -= 2
end = list(map(lambda y : int(y)+2, input().split()))
end[2] -= 2
visit = [[False] * (C+6) for _ in range(0,R+6)]
dp = [[2**31] * (C+6) for _ in range(0,R+6)]
answer = 2 ** 31

dfs(start[0], start[1], start[2], 0, False)

print(answer)
