# https://www.acmicpc.net/problem/4991
# 1 <= w, h <= 20

def bfs(s):
    start_r = dirty_list[s][0]
    start_c = dirty_list[s][1]
    
    queue = [[start_r,start_c]]
    count = 0
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]

            if arr[r][c] == '*' or arr[r][c] == 'o':
                for d in range(0,len_dirty):
                    if r == dirty_list[d][0] and c == dirty_list[d][1]:
                        rel[s][d] = count
                        rel[d][s] = count
                        for v in rel[s]:
                            if v == -1:
                                break
                        else:
                            return
                        break

            for d in dir:
                if R > r+d[0] and r+d[0] >= 0 and C > c + d[1] and c + d[1] >= 0 and arr[r+d[0]][c+d[1]] != 'x' and not visit[r+d[0]][c+d[1]]:
                    visit[r+d[0]][c+d[1]] = True
                    queue_.append([r+d[0], c+d[1]])

        queue = queue_
        count += 1

def find_shortest(now, total, count):
    global MIN
    count += 1
    if count == len_dirty:
        MIN = min(MIN, total)
        return

    for n in range (0,len_dirty-1):
        if not visit_d[n] and MIN >= total + rel[now][n]:
            visit_d[n] = True
            find_shortest(n, total + rel[now][n], count)
            visit_d[n] = False

dir = [[1,0], [-1,0], [0,1], [0,-1]]
while True:
    C, R = list(map(int, input().split()))
    if C == 0 and R == 0:
        break
    arr = []
    visit = [[False] * C for _ in range(0,R)]
    dirty_list = []
    start = []
    for r in range(0,R):
        line = input()
        arr_ = []
        for c in range(0,C):
            arr_.append(line[c])
            if line[c] == '*':
                dirty_list.append([r,c])
            elif line[c] == 'o':
                start = [r,c]
        arr.append(arr_)

    dirty_list.append(start)
    len_dirty = len(dirty_list)

    rel = [[-1] * len_dirty for _ in range(0,len_dirty)]

    for d in range(0,len_dirty-1):
        bfs(d)
        # visit 초기화
        for r in range(0,R):
            for c in range(0,C):
                visit[r][c] = False


    breakFlag = False
    for r in range(0,len_dirty):
        for c in range(0,len_dirty):
            if rel[r][c] == -1 and r != c:
                breakFlag = True
                break
        if breakFlag:
            break

    if breakFlag:
        print('-1')
    else:
        visit_d = [False] * len_dirty
        MIN = 999999999
        find_shortest(len_dirty-1, 0, 0)
        print(MIN)