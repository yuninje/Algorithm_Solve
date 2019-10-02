# https://www.acmicpc.net/problem/14002

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * len(arr)

MAX = 1
for i in range(1,len(arr)):
    d = 1
    for j in range(i):
        if arr[i] > arr[j]:
            d = max(dp[j]+1, d)    
    dp[i] = d
    MAX = max(MAX, d)

print(MAX)
M = MAX
answer = [-1] * (MAX+1)
for i in range(len(arr)-1, -1, -1):
    if dp[i] == M:
        if M != MAX:
            if arr[i] < answer[M+1]:    
                answer[M] = arr[i]
                M -= 1
        else:
            answer[M] = arr[i]
            M -= 1
            
del answer[0]
print(' '.join(list(map(str, answer))))   