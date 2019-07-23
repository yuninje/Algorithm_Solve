N, M = list(map(int, input().split()))
arr = [[0 for _ in range(0,M+1)]]
for n in range (0,N):
    arr.append([0] + list(map(int,input().split())))

K = int(input())

parts = []

for k in range(0,K):
    parts.append(list(map(int,input().split())))

dp = [[0 for _ in range(0,M+1)] for __ in range(0, N+1)]

for row in range(1, N+1):
    for col in range(1, M+1):
        dp[row][col] = dp[row][col-1] + arr[row][col]

for part in parts:
    sum = 0
    for p in range(part[0], part[2]+1):
        sum += dp[p][part[3]]
        sum -= dp[p][part[1]-1]
    print(sum)
