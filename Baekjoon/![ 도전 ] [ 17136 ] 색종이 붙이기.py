# https://www.acmicpc.net/submit/17135
# 10 * 10

def check(r_,c_):
    global ANSWER
    queue = [[r_,c_]]
    count = 1
    while queue:
        queue_ = []
        print(queue)
        for q in queue:
            r = q[0]
            c = q[1]
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                if N > rr and rr >= 0 and N > cc and cc >= 0 and arr[rr][cc] == 1:
                    if visit[rr][cc]:
                        continue
                    visit[rr][cc] = True
                    queue_.append([rr,cc])
                else:
                    print('취소===== r , c  : ' + str(rr) + ' ' + str(cc))
                    for q_ in queue_:
                        rrr = q_[0]
                        ccc = q_[1]
                        visit[rrr][ccc] = False
                    ANSWER += 1
                    return
        for q in queue:
            r = q[0]
            c = q[1]
            arr[r][c] = 0

        queue = queue_
        count += 1


N = 10
dir = [[1,0], [1,1], [0,1]]
arr = [list(map(int, input().split())) for _ in range(0, N)]
visit = [[False] * N for _ in range(0,N)]
ANSWER = 0
for r in range(0,N):
    for c in range(0,N):
        
        if arr[r][c] == 1 and not visit[r][c]:
            check(r, c)
print(ANSWER)