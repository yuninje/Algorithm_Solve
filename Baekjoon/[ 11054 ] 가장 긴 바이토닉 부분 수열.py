# https://www.acmicpc.net/problem/11054

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
dp_r = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if arr[i] > arr[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] +1
        
for i in range(N-2,-1,-1):
    for j in range(i+1,N):
        if arr[i] > arr[j] and dp_r[j] >= dp_r[i]:
            dp_r[i] = dp_r[j] +1
        
max = dp[0] + dp_r[0]
for i in range(1,N):
    if max < dp[i] + dp_r[i]:
        max = dp[i] + dp_r[i]

print(max-1)