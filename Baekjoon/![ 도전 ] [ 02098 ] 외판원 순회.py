# https://www.acmicpc.net/problem/2098
# 2 <= N <= 16
# 0 <= W[i][j] <= 1,000,000

def dfs(start, now, visit):
    # dp[visit] = INF
    
    MIN = INF
    print('start : ' + str(start) + '  now : ' + str(now) + '  visit : ' + bin(visit))
    
    if visit == FULL:
        return adj[now][start]
    
    for n in range(N):
        print('n : ' + str(n) + '   ', end = '')
        if visit & (1 << n) == 0:
            print('사용X')
            vv = visit + (1<<n)
            MIN = min(dfs(start, n, vv) + adj[now][n], MIN)
        else:
            print('사용O')
    return MIN

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
INF = 999999999
FULL = (1 << N) -1
answer = INF
dp = {}

for n in range(N):
    print(dfs(n,n,1<<n))
