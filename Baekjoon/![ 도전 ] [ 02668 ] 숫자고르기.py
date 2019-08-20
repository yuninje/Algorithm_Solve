# https://www.acmicpc.net/problem/2668
# 1 <= N <= 100

N = int(input())
arr = [0]
for n in range(0,N):
    arr.append(int(input()))
    
inner = [[0] * (N+1) for _ in range(0,N+1)]

for i in range(1,N+1):
    inner[arr[i]][i] = 1

for i in inner:
    print(i)