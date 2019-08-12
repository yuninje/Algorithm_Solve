# https://www.acmicpc.net/problem/2178
# 1 : move possible, 0 : move impossible
# (1,1) -> (N,M)
# 2 <= N, M <= 100

def bfs():
    queue = [[1,1]]
    count = 1
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            
            if r == N and c == M:
                return count
            if arr[r][c] == 0:
                continue
            if visit[r][c]:
                continue
            visit[r][c] = True
            for d in dir:
                queue_.append([r+d[0], c+d[1]])
        queue = queue_
        count += 1

N, M = list(map(int, input().split()))
dir = [[1,0], [-1,0], [0,1], [0,-1]]
arr = []
arr.append([0] * (M+2))
for n in range(1,N+1):
    line = input()
    a = [0]
    for c in range(0,M):
        a.append(int(line[c]))
    a.append(0)
    arr.append(a)

arr.append([0] * (M+2))
visit = [[False] * (M+2) for _ in range(0,N+2)]

print(bfs())