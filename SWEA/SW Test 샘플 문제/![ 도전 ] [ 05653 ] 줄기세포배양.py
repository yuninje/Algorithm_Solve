# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
# 22:40

def bfs():
    global queue
    time = 0
    while queue:
        queue_ = []
        del_list = []
        queue = sorted(queue, key= lambda x: area[x[0]][x[1]], reverse = True)
        print(queue)
        for q in range(0,len(queue)):
            r = queue[q][0]
            c = queue[q][1]
            if area[r][c][1] <= 0:
                if area[r][c][1] == -area[r][c][0]+1:
                    area[r][c] = [0,0]
                    del_list.append(q)
                for d in dir:
                    rr = r + d[0]
                    cc = c + d[1]
                    if area[rr][cc] == 0:
                        area[rr][cc] = [area[r][c][0], area[r][c][0]]
                        queue_.append([rr,cc])
            area[r][c][1] -= 1
        del_list = sorted(del_list, reverse=True)
        for d in del_list:
            del queue[d]
        queue += queue_
        time += 1
        if time == K:
            return len(queue)

dir = [[1,0], [-1,0], [0,1], [0,-1]]
T = int(input())
for test in range(1,T+1):
    R, C, K = list(map(int, input().split()))
    KK = K + 20
    arr = [list(map(int, input().split())) for _ in range(R)]
    area = [[0] * (KK + C) for _ in range(KK+R)]
    queue = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] != 0:
                area[r+KK//2][c+KK//2] = [arr[r][c], arr[r][c]] # 고정, 줄이기
                queue.append([r+KK//2,c+KK//2])
    print(bfs())