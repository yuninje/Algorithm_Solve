# https://www.acmicpc.net/problem/9251
arr = list(input())
brr = list(input())
dp = [0] * len(brr)

for a in arr:
    MAX = 0
    for i in range(len(brr)):
        b = brr[i]
        if a== b:
            if MAX < dp[i]:
                MAX = dp[i]
            else:
                dp[i] = MAX+1
        else:
            MAX = max(dp[i], MAX)
print(max(dp))    