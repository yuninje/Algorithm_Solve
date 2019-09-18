# https://www.acmicpc.net/problem/2261
# 2 ≤ n ≤ 100,000
# -10000 <= x, y <= 10000
import sys
I = sys.stdin.readline
N = int(I())
arr = {}
for n in range(N):
    x, y = map(int, I().split())
    if x in arr:
        arr[x] += [y]
    else:
        arr[x] = [y]

x_arr = list(arr.keys())
for x in x_arr:
    arr[x] = sorted(arr[x])
arr = sorted(arr.items())
print(arr)
MIN = 999999999
for a_x_idx in range(len(arr)):
    ax = arr[a_x_idx][0] 

    a_y_list = arr[a_x_idx][1]
    for a_y_idx in range(len(a_y_list)):
        ay = a_y_list[a_y_idx]
        if a_y_idx != len(a_y_list)-1:            # 같은 좌표
            MIN = min(MIN, (ay  - a_y_list[a_y_idx+1]) ** 2)

        # 다른좌표
        flag = False
        for b_x_idx in range(a_x_idx+1, len(arr)):
            bx = arr[b_x_idx][0]
            dif_x = (bx - ax)**2
            if dif_x >= MIN:
                break
            b_y_list = arr[b_x_idx][1]
            for by in b_y_list:
                dif_y = (by-ay) ** 2
                if flag and dif_y >= MIN:
                    break
                if dif_x + dif_y < MIN:
                    MIN = dif_x + dif_y
                    flag = True
print(MIN)