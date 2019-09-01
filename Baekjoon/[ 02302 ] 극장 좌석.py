# https://www.acmicpc.net/problem/2302
# 1 <= N <= 40

N = int(input())
M = int(input())
arr = [int(input()) for _ in range(M)]
arr.insert(0,0)
arr.append(N+1)
answer = 1
dp = [0,1,2,3]
for a in range(1,len(arr)):
    dif = arr[a]-arr[a-1]-1
    if len(dp) <= dif:
        for d in range(len(dp), dif+1):
            dp.append(dp[-1]+dp[-2])
    answer *= dp[dif]
print(answer) 
