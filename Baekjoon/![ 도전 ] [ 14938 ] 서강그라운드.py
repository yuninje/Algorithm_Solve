import sys
I = sys.stdin.readline

N, M, R = list(map(int, I().strip().split(' ')))
T = list(map(int, I().strip().split(' ')))
arr = [list(map(int, I().strip().split(' '))) for _ in range(R)]

print(arr)