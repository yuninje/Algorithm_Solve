# https://www.acmicpc.net/problem/9507
# 0 < T < 69
# 0 <= N <= 67
# n < 2     :: 1
# n == 2    :: 2
# n == 3    :: 4
# n > 3     :: koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)


T = int(input())
arr = [int(input()) for _ in range(T)]
dp = [1,1,2,4]
dp.append(dp[3] + dp[2] + dp[1] + dp[0])
max_arr = max(arr)
for m in range(5,max_arr+1):
    dp.append(dp[m-1] + dp[m-1] - dp[m-5]) # dp[m-5] + dp[m-4] + dp[m-3] + dp[m-2] + dp[m-1] - dp[m-5]

for a in arr:
    print(dp[a])
