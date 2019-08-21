# https://www.acmicpc.net/problem/1707
# 2 <= T (테스트케이스) <= 5
# 1 <= V (정점의 개수) <= 20000
# 1 <= E (간선의 개수) <= 200000
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline
def dfs(now, flag):
    global answer
    visit[now] = True
    arr[now] = flag
    for i in range(1,V+1):
        if inner[now][i]:
            if not visit[i]:
                dfs(i, not flag)
            else:
                if arr[i] == flag:
                    answer = 'No'
                    return
            if answer == 'No':
                return

T = int(I())
for test in range(1,T+1):
    V , E = list(map(int, I().split()))
    inner = [[False]*(V+1) for _ in range(0,V+1)]
    for e in range(0,E):
        line=list(map(int, I().split()))
        inner[line[0]][line[1]] = True
        inner[line[1]][line[0]] = True
    answer = 'Yes'
    arr = [False] * (V+1)
    visit = [False] * (V+1)
    for i in range(1,V+1):
        if not visit[i]:
            dfs(i, True)
    print(answer)
    print(sys.getsizeof(True))