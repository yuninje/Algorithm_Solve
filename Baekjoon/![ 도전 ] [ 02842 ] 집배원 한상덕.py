# https://www.acmicpc.net/problem/2842
# P : 우체국
# K : 집
# . : 목초지
# 우체국 ~   ~ 우체국
# 2 <= N <= 50
# 

def dfs(r,c):
    if dp[r][c][0] == 999999999 and dp[r][c][1] == -1:
        
    
    
    
    
    
    return dp[r][c]






dir = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
N = int(input())
aMap = [list(input()) for _ in range(N)]
nMap = [list(map(int,input().split())) for _ in range(N)]
towns = []
MIN, MAX = 999999999, -1
for r in range(N):
    for c in range(N):
        if aMap[r][c] == 'P':
            start = (r,c)
        elif aMap[r][c] == 'K':
            towns.append((r,c))
        else:
            continue
        MIN, MAX = min(nMap[r][c], MIN), max(nMap[r][c], MAX)
dp = [[[999999999, -1] for _ in range(N)] for __ in range(N)]
for r, c in towns:
    dfs(r,c)