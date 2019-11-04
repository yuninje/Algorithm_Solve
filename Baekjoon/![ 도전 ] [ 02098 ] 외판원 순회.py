# https://www.acmicpc.net/problem/2098
import time
start = time.time()
def dfs(start, now, visit):
    if visit & FULL == FULL:
        # print('visit full !!  visit : ' + bin(visit))
        if adj[now][start] == 0:
            return INF
        return adj[now][start]

    vv = visit | (now << N) | (start << (N+5) | 1 <<(N+10))
    # print('visit : ' + bin(visit) + '   vv : ' + bin(vv))
    if vv in dp:
        # print('dp use')
        return dp[vv]

    MIN = INF
    for n in range(N):
        if visit & (1 << n) != 0:
            continue
        if adj[now][n] == 0:
            continue
        MIN = min(MIN, adj[now][n] + dfs(start, n, visit | (1<<n)))

    dp[vv] = MIN
    return MIN


N = 8
adj = [[1] * N for _ in range(N)]

# N  = int(input())
# adj = [list(map(int, input().split())) for _ in range(N)]
INF = 999999999
FULL = (1 << N) -1
dp = dict()
answer = INF
for n in range(N):
    answer = min(answer, dfs(n,n,1<<n))
print('dp : ' + str(answer))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# for d in dp:
#     print(bin(d) + ' : ' + str(dp[d]))