# https://www.acmicpc.net/problem/2589

def bfs(r,c):
    global MAX
    visit = [[False] * C for _ in range(R)]
    visit[r][c] = True
    queue = [[r,c]]
    count = -1
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                if R > rr >= 0 and C > cc >= 0 and not visit[rr][cc] and arr[rr][cc] == 'L':
                    visit[rr][cc] = True
                    queue_.append([rr,cc])
        queue = queue_
        count += 1
    MAX = max(MAX, count)
dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, input().split()))
arr = [input() for _ in range(R)]
MAX = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'L':
            bfs(r,c)

print(MAX)