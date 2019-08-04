# 2 <= N <= 10
# 1 <= H <= 30
# 0 <= M <= (N-1) * H
import sys

def dfs(count, nowR,nowC):
        global answer
        count += 1
        if count != 0:
                if arr[nowR][nowC * 2] == 1:
                        return
                if nowC *2+2 <= C *2 +1:
                        if arr[nowR][nowC *2 +2] ==1:
                                return
                if nowC *2 -2 >= 0:
                        if arr[nowR][nowC * 2 -2] ==1:
                                return
                arr[nowR][nowC *2] = 1


        if check():
                if answer > count:
                        answer = count
                arr[nowR][nowC *2] = 0      
                return

        if count == 3:
                arr[nowR][nowC *2] = 0
                return

        # for r in range(1, R+1):
        #         for c in range(1,C):
        #                 dfs(count,r,c)

        for c in range(nowC+1,C):
                dfs(count, nowR, c)
        for r in range(nowR+1, R+1):
                for c in range(1,C):
                        dfs(count, r,c)

        arr[nowR][nowC *2] = 0
        
        
def check():
        for c in range(0,C):
                r_ = 0
                c_ = 2 * c +1
                while r_ != R+1:
                        r_ += 1
                        if arr[r_][c_+1] == 1:
                                c_ += 2

                        elif arr[r_][c_-1] == 1: 
                                c_ -= 2
        
        if c_ != 2 * c +1:
                return False
        return True
sys.setrecursionlimit(10**6)    # Maximum Recursion Dept Exceed

I = sys.stdin.readline
C, H, R = list(map(int, I().split()))

line_list = []
for h in range(0,H):
    line_list.append(list(map(int, I().split())))
# arr 의 가로 : C *2
# arr 의 세로 : R 
arr = [[0] * (C*2+1) for _ in range(0, R +2)]
for r in range(0,R+2):
    for c in range(0,C):
        arr[r][2*c+1 ] = 1

for l in line_list:
    arr[l[0]][l[1] *2] = 1

answer = 4
dfs(-1, 0,0)

if answer == 4:
        answer = -1
print(answer)