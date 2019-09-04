# https://www.acmicpc.net/problem/16236

def check():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue
            if arr[r][c] < level:
                return True
    return False

dir = [[-1,0], [0,-1], [0,1], [1,0]]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 0
visit = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            shark = (r,c)
            arr[shark[0]][shark[1]] = 0
level = 2
exp = 0
count = 0 # 총 시간
time = 0 # 찾은시간
queue = [shark]

while check() and queue:
    queue_ = []
    eat_list = []
    for r, c in queue:
        for dr, dc in dir:
            rr = r + dr
            cc = c + dc
            if N > rr and rr >= 0 and N > cc and cc >= 0 and not visit[rr][cc]:
                if arr[rr][cc] == 0:
                    visit[rr][cc] = True
                    queue_.append((rr,cc))
                elif arr[rr][cc] == level:
                    visit[rr][cc] = True
                    queue_.append((rr,cc))
                elif arr[rr][cc] < level:
                    eat_list.append((rr,cc))
    count += 1
    time += 1
    queue = queue_

    if eat_list:    
        eat_list = sorted(eat_list, key = lambda x: (x[0],x[1]))
        shark = eat_list[0]
        time = 0 
        exp += 1
        if exp == level:
            level += 1
            exp = 0
        queue = [shark]
        arr[shark[0]][shark[1]] = 0
        visit = [[False] * N for _ in range(N)]
print(count - time)