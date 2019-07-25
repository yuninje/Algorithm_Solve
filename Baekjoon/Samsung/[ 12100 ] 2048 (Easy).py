#https://www.acmicpc.net/problem/12100
import copy
def dfs(arr, count):
    if count == 5:
        return max(max(a) for a in arr)
        
    arr_left = move_left(copy.deepcopy(arr))
    left = dfs(arr_left, count+1)

    arr_right = move_right(copy.deepcopy(arr))
    right = dfs(arr_right, count+1)
    
    arr_up = move_up(copy.deepcopy(arr))
    up = dfs(arr_up, count+1)
        
    arr_down = move_down(copy.deepcopy(arr))
    down = dfs(arr_down, count+1)
    
    return max(right, left, up, down)

def move_left(arr):
    # 왼쪽으로 밀기
    for r in range(0,N):    
        for c in range(N-1,-1,-1):
            if arr[r][c] == 0:
                for c_ in range(c,N-1):
                    arr[r][c_] = arr[r][c_+1]
                arr[r][N-1] = 0
                c += 1
    # 합치기
    for r in range(0,N):
        for c in range(0,N-1):
            if arr[r][c] == arr[r][c+1]:
                arr[r][c] = arr[r][c] *2
                arr[r][c+1] = 0
    # 왼쪽으로 밀기
    for r in range(0,N):
        for c in range(N-1,-1,-1):
            if arr[r][c] == 0:
                for c_ in range(c,N-1):
                    arr[r][c_] = arr[r][c_+1]
                arr[r][N-1] = 0
                c += 1
    return arr


def move_right(arr):
    # 오른쪽으로 밀기
    for r in range(0,N):
        for c in range(0,N):
            if arr[r][c] == 0:
                for c_ in range(c, 0, -1):
                    arr[r][c_] = arr[r][c_-1]
                arr[r][0] = 0
                c -= 1
    # 합치기
    for r in range(0,N):
        for c in range(N-1, 0, -1):
            if arr[r][c] == arr[r][c-1]:
                arr[r][c] = arr[r][c] *2
                arr[r][c-1] = 0
    # 오른쪽으로 밀기
    for r in range(0,N):
        for c in range(0,N):
            if arr[r][c] == 0:
                for c_ in range(c, 0, -1):
                    arr[r][c_] = arr[r][c_-1]
                arr[r][0] = 0
                c -= 1
    return arr

def move_up(arr):
    # 위로 밀기
    for c in range(0,N):
        for r in range(N-1,-1,-1):
            if arr[r][c] == 0:
                for r_ in range(r,N-1):
                    arr[r_][c] = arr[r_+1][c]
                arr[N-1][c] = 0
                r += 1
    # 합치기
    for c in range(0,N):
        for r in range(0,N-1):
            if arr[r][c] == arr[r+1][c]:
                arr[r][c] = arr[r][c] *2
                arr[r+1][c] = 0
    # 위로 밀기
    for c in range(0,N):
        for r in range(N-1,-1,-1):
            if arr[r][c] == 0:
                for r_ in range(r,N-1):
                    arr[r_][c] = arr[r_+1][c]
                arr[N-1][c] = 0
                r += 1
    return arr

def move_down(arr):
    # 밑으로 밀기
    for c in range(0,N):
        for r in range(0,N):
            if arr[r][c] == 0:
                for r_ in range(r, 0, -1):
                    arr[r_][c] = arr[r_-1][c]
                arr[0][c] = 0
                r -= 1
    # 합치기
    for c in range(0,N):
        for r in range(N-1, 0, -1):
            if arr[r][c] == arr[r-1][c]:
                arr[r][c] = arr[r][c] *2
                arr[r-1][c] = 0
    # 밑으로 밀기
    for c in range(0,N):
        for r in range(0,N):
            if arr[r][c] == 0:
                for r_ in range(r, 0, -1):
                    arr[r_][c] = arr[r_-1][c]
                arr[0][c] = 0
                r -= 1
    return arr

#     return max(dfs(left), dfs(right), dfs(up), dfs(down))

#   1 <= N <= 20    0 : 빈칸       2<= block(2^n) <= 1024
N = int(input())

arr = []
for n in range(0,N):
    arr.append(list(map(int, input().split())))
answerList = []
print(dfs(arr, 0))