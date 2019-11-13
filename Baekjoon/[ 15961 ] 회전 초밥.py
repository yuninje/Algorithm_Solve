# https://www.acmicpc.net/problem/15961
# 접시수, 초밥의 가짓수, 연속 접시수, 쿠폰번호
import sys
I = sys.stdin.readline
N, D, K, C = list(map(int, I().split()))
arr = [int(I()) for _ in range(N)]
counts = [0] * (D+1)
count = 0

for i in range(K):
    counts[arr[i]] += 1

for i in range(1,D+1):
    if counts[i] > 0:
        count += 1

if counts[C] == 0:
    answer = count+1
else:
    answer = count

for i in range(K, N+K):
    counts[arr[i%N]] += 1
    if counts[arr[i%N]] == 1:
        count += 1
    
    counts[arr[i-K]] -= 1
    if counts[arr[i-K]] == 0:
        count -= 1
    
    if counts[C] == 0:
        answer = max(answer, count+1)
    else:
        answer = max(answer, count)

print(answer)