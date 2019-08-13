# https://www.acmicpc.net/problem/2468
# True : safe
# False : not safe

import sys
sys.setrecursionlimit(10**6)
def dfs(r,c):
    if not blist[r][c]:
        return
    blist[r][c] = False

    for d in dir:
        dfs(r+d[0] , c + d[1])


N = int(input())
dir = [[1,0], [-1,0], [0,1], [0,-1]]
arr = []
for n in range(0,N):
    arr.append(list(map(int, input().split())))
    
MAX = 0
for h in range(0, 101):
    count = 0
    blist = [[False] * (N+2) for _ in range(0,N+2)]
    for r in range(0,N):
        for c in range(0,N):
            if arr[r][c] > h:
                blist[r+1][c+1] = True 

    for r in range(1,N+1):
        for c in range(1,N+1):
            if blist[r][c]:
                count += 1
                dfs(r,c)
    if MAX < count:
        MAX = count
print(MAX)
