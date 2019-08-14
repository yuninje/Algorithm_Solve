import sys
I = sys.stdin.readline

arr = []
MAX = 0
N = int(I())
while N != 0:
    arr.append(N)
    MAX = max(MAX, N)
    N = int(I())

dp = [0,1]
sum = [0,1]
# dp[n] = sum[n-1] + dp[n-1] + 1
for n in range(2,MAX+1):
    dp.append(sum[n-1] + dp[n-1] + 1)
    sum.append(sum[n-1] + dp[n])


print("dp=======================")
print(dp)

print("sum================================")
print(sum)
# for a in arr:
#     print(dp[a])