# https://www.acmicpc.net/problem/11399
# 1 <= N <= 1000

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
answer = 0
for n in range(N):
    answer += arr[n] * (N-n)
print(answer)