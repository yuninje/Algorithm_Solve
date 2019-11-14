# https://www.acmicpc.net/problem/15686
# 2 <= N <= 50
# 1 <= M <= 13
# 0 : 빈칸
# 1 : 집
# 2 : 치킨집

import sys
I = sys.stdin.readline

def combination(now, count):
    global answer
    if count == M:
        # 작업
        result = 0
        for r,c in homes:
            dist = 999999999
            for i in range(len(chi_home)):
                if exist[i]:
                    dist = min(dist, dp[r][c][i])
            result += dist
        answer = min(answer, result)
        return

    if now == len(chi_home):
        return

    combination(now+1, count)
    exist[now] = True
    combination(now+1, count+1)
    exist[now] = False

dir = [[1,0], [-1,0], [0,1], [0,-1]]
N, M = list(map(int, I().split()))
Map = [list(map(int, I().split())) for _ in range(N)]


homes = []
chi_home = []
# naming
for r in range(N):
    for c in range(N):
        if Map[r][c] == 1:
            homes.append((r,c))
        elif Map[r][c] == 2:
            chi_home.append((r,c))
# combination
exist = [False] * len(chi_home)
dp = [[[999999999] * len(chi_home) for __ in range(N)] for _ in range(N)]
for i in range(len(chi_home)):
    cr, cc = chi_home[i]
    for r in range(N):
        for c in range(N):
            dp[r][c][i] = abs(cr - r) + abs(cc - c)
answer = 999999999
combination(0,0)
print(answer)