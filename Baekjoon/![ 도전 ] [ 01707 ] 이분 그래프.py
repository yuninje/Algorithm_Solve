# https://www.acmicpc.net/problem/1707
# 2 <= T (테스트케이스) <= 5
# 1 <= V (정점의 개수) <= 20000
# 1 <= E (간선의 개수) <= 200000
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

T = int(input())
answers = [0] * T
for test in range(T):
    V , E = list(map(int, I().strip().split()))
    inner = [[] for _ in range(0,V+1)]
    for _ in range(0,E):
        a, b=list(map(int, I().strip().split()))
    

for a in answers:
    print(a)