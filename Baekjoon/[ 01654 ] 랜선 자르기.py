# https://www.acmicpc.net/problem/1654
# 1 <= K <= 10000
# 1 <= N <= 1000000
import sys
I = sys.stdin.readline
K, N = list(map(int, I().split()))
arr = [int(I()) for _ in range(K)]

total = 0
for a in arr:
    total += a

MAX = total // N
answer = 0

start = 1
end = MAX
while start < end:
    mid = (start + end) // 2
    t = 0
    for a in arr:
        t += a // mid
    if t < N:
        end = mid
    else:
        start = mid+1

print(start-1)