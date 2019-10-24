# https://www.acmicpc.net/problem/1753
# 1 <= N ( 정점 ) <= 20,000
# 1 <= L ( 간선 ) <= 300,000


def bfs(s):
    result = [0] * (V+1)

    que = [s]

    while que:
        que_ = []
        for q in que:
            


        que = que_


    return result

V, E = list(map(int, input().split()))
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
INF = 999999999
dist = [{} for _ in range(V+1)]

for s, e, v in arr:
    if e in dist[s]:
        dist[s][e] = min(dist[s][e], v)
    else:
        dist[s][e] = v 

result = bfs(K)

print(result)

for d in range(1,V+1):
    print(str(d) + ' :: ' + str(dist[d]))

