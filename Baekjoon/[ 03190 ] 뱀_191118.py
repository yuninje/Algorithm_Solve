# https://www.acmicpc.net/problem/3190
# 2 <= N <= 100
# 0 <= A <= 100
# 1 <= D <= 100
#       우     하      좌      상
dir = [[0,1], [1,0], [0,-1], [-1,0]]
N = int(input())
A = int(input())
arr = [list(map(int, input().split())) for _ in range(A)]
D = int(input())
drr = [input().split() for _ in range(D)]
for d in range(D):
    drr[d][0] = int(drr[d][0])
Map = [[5] * N for _ in range(N)]
snake = [(0,0,0)]
sr, sc, d = snake[0]
time = 0
ti = 0
while 0 <= sr < N and 0 <= sc < N:
    for s in range(len(snake)):
        rr, cc, d = snake[s]
        rr += dir[d][0]
        cc += dir[d][1]
        if 0 <= rr < N and 0 <= cc < N:
            if Map[rr][cc] != 5:
                d = Map[rr][cc]
            snake[s] = sr,sc,d
        else:
            return time
    time += 1
    sr,sc,d = snake[0]
    if drr[ti][0] == time:
        if drr[ti][1] == 'L':
            d = ( d + 4 - 1 ) % 4
        else:
            d = ( d + 4 + 1 ) % 4
        ti += 1
        Map[sr][sc] = d
    snake[0] = sr,sc,d

print(time)
