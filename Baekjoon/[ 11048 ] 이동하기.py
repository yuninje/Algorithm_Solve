# https://www.acmicpc.net/problem/11048
N, M = list(map(int, input().split()))

arr = [[0 for _ in range(0,M+1)]]
for n in range(0,N):
    arr.append([0] + list(map(int, input().split())))

# for a in arr:
#     print(a)

dp = [[0 for _ in range(0,M+1)] for __ in range(0,N+1)]

for n in range(1,N+1):
    for m in range(1, M+1):
        dp[n][m] = max(dp[n-1][m], dp[n][m-1]) + arr[n][m]

print(dp[N][M])