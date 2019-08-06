# https://www.acmicpc.net/problem/11722

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
for n in range(1,N):
    for d in range(0,n):
        if  arr[d] > arr[n] and dp[d] >= dp[n]:
            dp[n] = dp[d] + 1

print(max(dp))