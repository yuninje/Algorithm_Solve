# https://www.acmicpc.net/problem/9376
# 2 <= R, C <= 100
# . : 빈공간
# * : 벽
# # : 문
# $ : 죄수
import sys
I = sys.stdin.readline
dir = [[1,0], [-1,0], [0,1], [0,-1]]

T = int(I())
answers = [0] * T
for t in range(T):
    R, C = list(map(int, I().split()))
    Map = [list(I()) for _ in range(R)]
    
    
