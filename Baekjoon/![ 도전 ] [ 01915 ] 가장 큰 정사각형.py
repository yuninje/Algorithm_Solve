# https://www.acmicpc.net/problem/1915
# 1 <= R, C <= 1000
import sys
sys.setrecursionlimit(10 ** 6)
I = sys.stdin.readline

def bfs(r_, c_):
    global MAX
    count = 1
    queue = [[r_, c_]]
    while queue:
        queue_ = []
        for q in queue:
            r = q[0]
            c = q[1]
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                if R > rr and rr >= 0 and C > cc and cc >= 0:
                    if arr[rr][cc] == '0':
                        MAX = max(MAX, count)
                        return
                    queue_.append([rr, cc])
        queue = queue_
        count += 1

dir = [[0,1], [1,0], [1,1]]
R, C = list(map(int, I().split()))
arr = ['0'*(C+2)]
for r in range(0,R):
    arr.append('0'+I()+'0')
arr.append('0'*(C+2))

MAX = 0
one_flag = False
for r in range(1,R+1):
    for c in range(1,C+1):
        if arr[r][c] == '1':
            one_flag = True
            bfs(r, c)
for a in arr:
    print(a)

if one_flag and MAX == 0:
    print(1)
else:
    print(MAX * MAX)