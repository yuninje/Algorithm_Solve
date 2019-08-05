# https://www.acmicpc.net/problem/2580

arr = [[]]
list0 = []
for r in range(1,10):
    arr.append([0] + list(map(int, input().split())))
    for c in range(1,10):
        if arr[r][c] == 0:
            list0.append([r,c])

# 가로 체크
for r in range(1,10):
    for c in range(1,10):

# 세로 체크

# 3 * 3 체크
