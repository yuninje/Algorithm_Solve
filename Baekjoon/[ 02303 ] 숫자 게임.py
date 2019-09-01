# https://www.acmicpc.net/problem/2303
import sys
sys.setrecursionlimit(10**6)

def dfs(person, before, count, total):
    global MAX_P
    if count == 3:
        MAX_P = max(MAX_P, total)
    for i in range(before+1, 5):
        dfs(person, i, count + 1, (total + arr[n][i])%10)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX = -1
MAX_INDEX = -1
for n in range(N):
    MAX_P = -1
    dfs(n, -1, 0, 0)
    if MAX <= MAX_P:
        MAX_INDEX = n
        MAX = MAX_P

print(MAX_INDEX+1)