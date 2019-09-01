# https://www.acmicpc.net/problem/2999
# N글자
# R <= C and R * C = N 
# N <= 100
# 
import math
a = input()
N = len(a)
R = 0
C = 0

for r in range(int(math.sqrt(N)), 0, -1):
    for c in range(int(math.sqrt(N)),N+1):
        if r <= c and r * c == N:
            R, C = r,c
            break
    if R != 0 and C != 0:
        break
arr = [[0] * C for _ in range(0,R)]
idx = 0
for c in range(0,C):
    for r in range(0,R):
        arr[r][c] = a[idx]
        idx += 1

result = ''
idx = 0
for r in range(0,R):
    for c in range(0,C):
        result += arr[r][c]

print(result)