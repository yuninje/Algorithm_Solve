# 0 : 0
# 1 : 폭탄 주위
# 2 : 폭탄 주위 처리

def bfs(r,c):
    que = [(r,c)]
    Map[r][c] = -1
    while que:
        que_ = []
        for r, c in que:
            for dr,dc in dir:
                rr = r + dr
                cc = c + dc
                if 0 <= rr and rr < N and 0 <= cc and cc < N:
                    if Map[rr][cc] == 1:
                        Map[rr][cc] = -1
                    elif Map[rr][cc] == 0:
                        Map[rr][cc] = -1
                        que_.append((rr,cc))
        que = que_


def check(r,c):
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if 0 <= rr and rr < N and 0 <= cc and cc < N:
            if Map[rr][cc] == '*':
                return False

    return True


dir = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1, 0), (-1,-1)]

T = int(input())
for test in range(1,T+1):
    N = int(input())
    Map = [list(input()) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if Map[r][c] == '*':
                for dr, dc in dir:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr and rr < N and 0 <= cc and cc < N:
                        if Map[rr][cc] != '*':
                            Map[rr][cc] = 1
            elif Map[r][c] == '.':
                Map[r][c] = 0

    for r in range(N):
        for c in range(N):
            if Map[r][c] == 0:
                bfs(r,c)
                answer += 1
    
    for r in range(N):
        for c in range(N):
            if Map[r][c] == 1:
                answer += 1
    print('#' + str(test) + ' ' + str(answer))