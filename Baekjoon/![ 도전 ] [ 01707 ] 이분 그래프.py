# https://www.acmicpc.net/problem/1707
# 2 <= T (테스트케이스) <= 5
# 1 <= V (정점의 개수) <= 20000
# 1 <= E (간선의 개수) <= 200000
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def dfs(now, flag):
    global answerFlag
    arr[now] = flag
    for a in inner[now]:
        if arr[a] == 0:
            dfs(a, -flag)
        elif arr[a] == flag:
            answerFlag = True
        if answerFlag:
            return

def bfs(now):
    global noFlag
    arr[now] = 1
    queue = [now]
    while queue:
        queue_ = []
        for q in queue:
            flag = arr[q]
            for i in inner[q]:
                if arr[i] == flag:
                    noFlag = True
                    return
                elif arr[i] == 0:
                    arr[i] = -flag
                    queue_.append(i)
                
        queue = queue_
        
T = int(input())
for test in range(1,T+1):
    V , E = list(map(int, input().split()))
    inner = [[] for _ in range(0,V+1)]
    for _ in range(0,E):
        a, b=list(map(int, input().split()))
        inner[a].append(b)
        inner[b].append(a)
    noFlag = False
    arr = [0] * (V+1)
    for i in range(1,V+1):
        if arr[i] == 0:
            bfs(i)
        if noFlag:
            break
    if noFlag:
        print('No')
    else:
        print('Yes')