# https://www.acmicpc.net/problem/16234
# 1 <= N <= 50
# 1 <= L <= R <= 100
# 1 <= Map[r][c] <= 100

# 79% 시간터짐

import sys
I = sys.stdin.readline

def calAvg(group):
    total = 0
    for r, c in group:
        total += Map[r][c]
    return total // len(group)


def resetVisit():
    for r in range(N):
        for c in range(N):
            visit[r][c] = False


def bfs(r, c):
    que = [(r, c)]
    visit[r][c] = True
    group = []

    while que:
        que_ = []
        for r, c in que:
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if 0 <= rr < N and 0 <= cc < N:
                    if L <= abs(Map[r][c] - Map[rr][cc]) <= R:
                        if visit[rr][cc]:
                            continue
                        que_.append((rr, cc))
                        visit[rr][cc] = True
        group += que
        que = que_
    return group


def fun():
    count = 0
    while(True):
        resetVisit()
        flag = False
        for r in range(N):
            for c in range(N):
                # print('r : ' + str(r) + '  c : ' + str(c))
                if visit[r][c]:
                    continue
                group = bfs(r, c)
                if len(group) > 1:
                    flag = True
                    avg = calAvg(group)
                    for gr, gc in group:
                        Map[gr][gc] = avg
        if not flag:
            return count
        count += 1

N, L, R = map(int, I().split())
Map = [list(map(int, I().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
print(fun())
