# https://www.acmicpc.net/problem/1202
# 1 <= N, K <= 300,000
# 0 <= M[i] , V[i] <= 1,000,000
# 1 <= C[i] <= 100,000,000

import sys
I = sys.stdin.readline
N, K = map(int, I().split())
J = [list(map(int, I().strip().split())) for _ in range(N)]
B = [int(I().strip()) for _ in range(K)]

J = sorted(J, key = lambda x : x[1])
B = sorted(B)

