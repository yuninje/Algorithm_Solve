# https://www.acmicpc.net/problem/11724

# N : 정점의 개수   1 <= N <= 1000
# M : 간선의 개수   0 <= M <= N * (N-1) / 2
# 양 끝점 u, v      1 <= u, v <= N. (u != v)
import sys
sys.setrecursionlimit(10**6)

def dfs(now):
    if bool_list[now]:
        return
    bool_list[now] =True
    for a in range(0,len(arr),1):
        if arr[a][0] == now:
            dfs(arr[a][1])
            del arr[a]
            a -= 1
        elif arr[a][1] == now:
            dfs(arr[a][0])
            del arr[a]
            a -= 1

N, M = list(map(int, input().split()))
arr = []
for m in range(0,M):
    arr.append(list(map(int, input().split())))

bool_list = [False for _ in range(0,N+1)]
answer = 0
for n in range(1,N+1):
    if not bool_list[n]:
        dfs(n)
        answer += 1
print(answer)