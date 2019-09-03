# https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    answer = 0
    
    dp = [[10001] * (N+1) for _ in range(N+1)]
    inner = [[10001] * (N+1) for _ in range(N+1)]
    road = sorted(road, key = lambda x : x[2])

    for r in road:
        if inner[r[0]][r[1]] == 10001:
            inner[r[0]][r[1]] = r[2]
            inner[r[1]][r[0]] = r[2]
    
def dfs(now, N, dp, inner):

    for i in range(2,N+1):
        if inner[now][i] == 0:
            continue
        dfs(i, total, N, dp, inner)
