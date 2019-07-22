N = int(input())

arr = [0] + list(map(int,input().split()))

dp = []
dp.append(0)
dp.append(1)

for i in range(2,N+1):
    min = 0
    for j in range(0,i):
        if arr[i] > arr[j] and min < dp[j]:
            min = dp[j]
    
    dp.append(min+1)

print(max(dp))