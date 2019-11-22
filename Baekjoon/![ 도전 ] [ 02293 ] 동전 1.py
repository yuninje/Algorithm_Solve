# https://www.acmicpc.net/problem/2293
# 1 <= N <= 100
# 1 <= K <= 10,000
# 1 <= COIN(n) <= 100,000

N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]
