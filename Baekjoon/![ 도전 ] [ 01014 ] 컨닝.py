# https://www.acmicpc.net/problem/1014
import sys
I = sys.stdin.readline



def aroundCount(r,c):
    count = 0
    for dr, dc in dD:
        rr, cc = r + dr, c + dc
        if not (0 <= rr < R and 0 <= cc < C):
            continue
        if Map[rr][cc] == '.':
            count += 1
    return count

def changeAround(r,c):
    Map[r][c] = 'O'
    for dr, dc in dD:
        rr, cc = r + dr, c + dc
        if not (0 <= rr < R and 0 <= cc < C):
            continue
        if Map[rr][cc] == '.':
            Map[rr][cc] = 'N'

def dfs(status, a, b):
    global answer 
    if not status:
        for r in range(R):
            for c in range(C):
                if Map[r][c] == '.':
                    Map[r][c] = 'N'
                    dfs(True, r, c)

                    Map[r][c] = 'O'
                    for dr, dc in dD:
                        rr, cc = r + dr, c + dc
                        if not (0 <= rr < R and 0 <= cc < C):
                            continue
                        Map[rr][cc] = 'N'
                    dfs(True, r, c)
                    return

    existFlag = False
    changeFlag = False
    for r in range(a, R):
        for c in range(C):
            if Map[r][c] =='.':
                existFlag = True
                cal = aroundCount(r,c)
                if cal == 1:
                    changeAround(r,c)
                    changeFlag = True
    if existFlag:
        dfs(changeFlag,0,0)
    else:
        count = 0
        print('=======================================')
        for m in Map:
            print(m)
        for r in range(R):
            for c in range(C):
                if Map[r][c] =='O':
                    count += 1
        answer = max(answer, count)

dD = [[1,1],[1,-1],[0,1],[0,-1],[-1,1],[-1,-1]]
dE = [[0,1],[0,-1]]                  
T = int(I())
answers = [0] * T

for t in range(T):
    R, C= map(int, I().split())
    Map = [list(I().strip()) for _ in range(R)]
    answer = 0
    dfs(True, 0,0)
    answers[t] = answer
        

for a in answers:
    print(a)