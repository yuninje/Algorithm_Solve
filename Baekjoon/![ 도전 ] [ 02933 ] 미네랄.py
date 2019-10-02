# https://www.acmicpc.net/problem/2933
# . : 빈칸, x : 미네랄
import sys
I = sys.stdin.readline

def dfs(r,c):
    # 붙어있는지 확인
    


dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
Map = [I().split() for _ in range(R)]
N = int(I())
arr = list(map(int, I().split()))


for a in arr: