# https://www.acmicpc.net/problem/11052
# 카드 1개, 두개, ... N개   >> 총 N가지
# 

N = int(input())
arr = [0] + list(map(int, input().split()))


# 카드 갯수당 최대 무게 dp

dp = [0]
dp.append(arr[1])
dp.append(max(dp[1] * 2 , arr[2]))

for i in range(3,N+1):
    max = arr[i]
    for j in range(1,i):
        if max <= dp[j] + dp[i-j]:
            max = dp[j] + dp[i-j]


    dp.append(max)

print(dp[N])