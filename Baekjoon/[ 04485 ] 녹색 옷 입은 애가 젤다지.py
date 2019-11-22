# https://www.acmicpc.net/problem/4485
from queue import PriorityQueue
import sys
I = sys.stdin.readline

MAX = 125
INF = 999999999
dir = [[1,0],[-1,0], [0,1],[0,-1]]
Map = [[0] * MAX for _ in range(MAX)]
dp = [[INF] * MAX for _ in range(MAX)]
for test in range(1, INF):
    N = int(I())
    if N == 0:
        break
    for r in range(N):
        line = list(map(int, I().split()))
        for c in range(N):
            Map[r][c] = line[c]
            dp[r][c] = INF
    pq = PriorityQueue()

    pq.put((Map[0][0], 0,0))
    while not pq.empty():
        v, r, c = pq.get()
        if dp[r][c] == INF:
            dp[r][c] = v
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not ( 0 <= rr < N and 0 <= cc < N ) or dp[rr][cc] != INF:
                    continue
                pq.put((v + Map[rr][cc], rr, cc))

        if r == N-1 and c == N-1:
            break


    print('Problem ' + str(test) + ': ' + str(dp[N-1][N-1]))