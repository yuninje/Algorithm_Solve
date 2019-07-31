# https://www.acmicpc.net/problem/11724   
# PyPy3
# N : 정점의 개수   1 <= N <= 1000
# M : 간선의 개수   0 <= M <= N * (N-1) / 2
# 양 끝점 u, v      1 <= u, v <= N. (u != v)

import sys
sys.setrecursionlimit(10**6)

def dfs(now):
    if bool_list[now]:
        return
    bool_list[now] =True

    for n in range(1,N+1):
        if arr[now][n] == 1:
            dfs(n)

N, M = list(map(int, input().split()))
arr = [[0]*(N+1) for __ in range(0,N+1)]
for m in range(0,M):
    a = list(map(int, sys.stdin.readline().split()))
    arr[a[0]][a[1]] = 1
    arr[a[1]][a[0]] = 1

bool_list = [False] * (N+1)
answer = 0
for n in range(1,N+1):
    if not bool_list[n]:
        dfs(n)
        answer += 1
print(answer)