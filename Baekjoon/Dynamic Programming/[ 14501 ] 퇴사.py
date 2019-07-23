N = int(input())

arr = [[0,0]]
for n in range(0,N):
    arr.append(list(map(int, input().split())))
dp = [[0,0] for _ in range(0,N+1)]

#[Time,Pay]
max = 0

for i in range(1,N+1):
    for j in range(1,i):
        if dp[j][0] <= i and dp[i][1] < dp[j][1]:
            dp[i][1] = dp[j][1]

    if(i + arr[i][0] <= N+1):
        dp[i][0] = i + arr[i][0]
        dp[i][1] += arr[i][1]
    
    if max < dp[i][1]:
        max = dp[i][1]


print(max)