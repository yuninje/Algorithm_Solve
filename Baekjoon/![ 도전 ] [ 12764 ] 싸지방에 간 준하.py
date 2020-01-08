# https://www.acmicpc.net/problem/12764
# 1 <= N <= 100,000
# 0 <= P < Q <= 1,000,000
from queue import PriorityQueue
import sys
I = sys.stdin.readline
N = int(I())
arr = [list(map(int, I().split())) for _ in range(N)]
