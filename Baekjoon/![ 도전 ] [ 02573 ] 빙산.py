# https://www.acmicpc.net/problem/2573
# 0 <= Map[r][c] <= 10
# 3 <= R, C <= 300
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

R, C = map(int, I().split())
Map = [list(map(int, I().split())) for _ in range(R)]