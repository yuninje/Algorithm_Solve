# https://www.acmicpc.net/problem/17135
# 3 <= R, C <= 15
# 1 <= D <= 10

def game():
    count = 0
    for i in range(0,R):
        target = []
        for a in archer:
            target.append(find(a[0],a[1]))
        for t in target:
            if t[0] == -1 and t[1] == -1:
                continue
            elif arr[t[0]][t[1]] == 1:
                arr[t[0]][t[1]] = 0
                count += 1
        
        exitFlag = False

        for r in range(1,R):
            for c in range(0,C):
                arr[R-r][c] = arr[R-r-1][c]
                if arr[R-r][c] == 1:
                    exitFlag = True
        for c in range(0,C):
            arr[0][c] = 0    
        if not exitFlag:
            return count

    return count

def select():
    global ANSWER
    global archer
    for i in range(0,C-2):
        for j in range(i+1, C-1):
            for k in range(j+1,C):
                archer = []
                archer.append([R,i])
                archer.append([R,j])
                archer.append([R,k])
                set_arr()
                reset_visit()
                result = game()
                ANSWER = max(ANSWER, result)

def find(archerR,archerC):
    reset_visit()
    count = 1
    queue = [[archerR-1, archerC]]
    while count <= D:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            if arr[r][c] == 1:
                return [r,c]
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                if C > cc and cc >= 0 and rr >= 0 and not visit[rr][cc]:
                    visit[rr][cc] = True
                    queue_.append([rr,cc])
        queue = queue_
        count += 1
    return [-1, -1]


def set_arr():
    for r in range(0,R):
        for c in range(0,C):
            arr[r][c] = area[r][c]
def reset_visit():
    for r in range(0,R):
        for c in range(0,C):
            visit[r][c] = False
    


dir = [[0,-1],[-1,0], [0,1]]
R, C, D = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(0,R)]
arr = [[0] * C for _ in range(0,R)]
visit = [[False] * C for i in range(0,R)]
archer = []
ANSWER = 0
select()

print(ANSWER)