# https://www.acmicpc.net/problem/2798

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
MAX = 0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            total = arr[i] + arr[j] + arr[k]
            if total <= M:
                MAX = max(MAX, total)

print(MAX)