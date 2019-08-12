# https://www.acmicpc.net/problem/2583
# N,M,K <= 100
import sys
sys.setrecursionlimit(10**6)    # Maximum Recursion Dept Exceed
def dfs(r,c, first):
    global count
    if first:
        count = 0
    if arr[r][c] == 1:
        return
    arr[r][c] = 1
    count += 1

    for d in dir:
        dfs(r+d[0], c+d[1], False)

    if first:
        countList.append(count)

N, M, K = list(map(int, input().split()))
dir = [[1,0], [-1,0], [0,1], [0,-1]]

arr = [[1] * (M+2) for _ in range(0,N+2)]
for r in range(1,N+1):
    for c in range(1,M+1):
        arr[r][c] = 0

square = []
for k in range(0,K):
    s = list(map(lambda x:int(x)+1, input().split()))
    for r in range(s[1], s[3]):
        for c in range(s[0], s[2]):
            arr[r][c] = 1

countList = []
count = 0
for r in range(1,N+1):
    for c in range(1,M+1):
        if arr[r][c] == 0:
            dfs(r,c,True)

print(len(countList))
for c in sorted(countList):
    print(c, end=' ')