# https://www.acmicpc.net/problem/1300
# N * N ( 1부터 시작 )
# A[i][j] = i * j
# N <= 100000,  K <= min(1,000,000,000 , N * N)

N = int(input())
K = int(input())

Map = [[0] * (N) for _ in range(N)]

for r in range(N):
    for c in range(N):
        Map[r][c] = (r+1) * (c+1)

idx = [0] * N

for k in range(K):
    Min = 1000000001
    for n in range(N):
        if idx[n] < N and Min > Map[n][idx[n]]:
            Min = Map[n][idx[n]]
            Min_idx = n
    idx[Min_idx] += 1

print(Min)