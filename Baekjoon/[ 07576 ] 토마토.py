# https://www.acmicpc.net/problem/7576
# 2 <= M, N <= 1000
# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토 X

import sys
import collections
I = sys.stdin.readline

def bfs():
    global count0
    day = 0
    count = len(deq)
    while deq:
        if count == 0:
            count = len(deq)
            day += 1

        now = deq.popleft()
        
        count -= 1

        if day != 0:
            count0 -= 1
        
        if count0 == 0:
            return day
        for d in dir:
            r = now[0]+d[0]
            c = now[1]+d[1]
            if r < N and r >= 0 and c < M and c >= 0 and  arr[r][c] == 0:
                arr[r][c] = 1
                deq.append([r,c])
    return -1

M, N = list(map(int, I().split()))

dir = [[1,0],[-1,0],[0,1],[0,-1]]
deq = collections.deque()
arr = []
count0 = 0
for r in range(0,N):
    arr.append(list(map(int, I().split())))
    for c in range(0,M):
        if arr[r][c] == 1:
            deq.append([r,c])
        elif arr[r][c] == 0:
            count0 += 1

print(bfs())