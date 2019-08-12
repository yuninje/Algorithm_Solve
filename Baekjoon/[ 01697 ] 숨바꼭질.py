# https://www.acmicpc.net/problem/1697
def bfs():
    second = 0
    queue = [N]
    while queue:
        queue_ = []
        for q in queue:
            if visit[q]:
                continue
            visit[q] = True
            if q == K:
                return second

            if q+1 <= 100000:
                queue_.append(q + 1)
            if q-1 >= 0:
                queue_.append(q - 1)
            if q * 2 <= 100000:
                queue_.append(q * 2)
        
        queue = queue_
        second += 1


N, K = list(map(int, input().split()))
visit = [False] * 100001
print(bfs())
