# https://www.acmicpc.net/problem/17472

def dfs(r,c,idx):       # 이름 지어주기
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if 0 <= rr and rr < R and 0 <= cc and cc < C:    
            if arr[rr][cc] == 1:
                arr[rr][cc] = idx
                dfs(rr,cc,idx)

def bfs(idx):           # idx 섬으로 부터 각 섬까지의 거리
    que = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] == idx:
                for d in range(4):
                    rr = r + dir[d][0]
                    cc = c + dir[d][1]
                    if 0 <= rr and rr < R and 0 <= cc and cc < C:
                        que.append([rr,cc, d])
    count = 0
    while que:
        que_ = []

        for r,c,d in que:
            rr = r + dir[d][0]
            cc = c + dir[d][1]
            if arr[r][c] == 0:
                if 0 <= rr and rr < R and 0 <= cc and cc < C:
                    que_.append([rr,cc,d])
            else:
                if arr[r][c] == idx:
                    continue
                if count < 2:
                    continue
                if inner[idx][arr[r][c]] == 0:
                    inner[idx][arr[r][c]] = count

        que = que_
        count += 1


dir = [[-1,0], [1,0], [0,-1], [0,1]]
R, C = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]

idx = 2
for r in range(R):
    for c in range(C):
        if arr[r][c] == 1:
            arr[r][c] = idx
            dfs(r,c, idx)
            idx += 1

inner = [[0] * idx for _ in range(idx)]     # 인접 배열

for i in range(2,idx):                      #  i 섬에서 다른 섬까지의 거리
    bfs(i)

brr = []                                    # A, B, V : A에서 B까지의 거리는 V

for r in range(2,idx):
    for c in range(r+1,idx):
        if inner[r][c] == 0:
            continue
        brr.append([r,c,inner[r][c]])

brr = sorted(brr, key= lambda x: x[2])

crr = []
visit = [-1] * idx
answer = 0

for a, b, v in brr:                         # 유니온같은거

    va = visit[a]
    vb = visit[b]
    if va == -1 and vb == -1:
        visit[a] = len(crr)
        visit[b] = len(crr)
        crr.append([a,b])
    elif va == -1:       # va 만 0
        visit[a] = vb
        crr[vb].append(a)
    elif vb == -1:       # vb 만 0
        visit[b] = va
        crr[va].append(b)
    else:
        if va == vb:
            continue
        else:
            if va < vb: # vb > va
                for b_ in crr[vb]:
                    visit[b_] = va
                crr[va] += crr[vb]
                crr[vb] = []
            else:   # va > vb
                for a_ in crr[va]:
                    visit[a_] = vb
                crr[vb] += crr[va]
                crr[va] = []
    answer += v

if crr:
    if len(crr[0]) != idx-2:
        print('-1')
    else:
        print(answer)
else:
    print('-1')