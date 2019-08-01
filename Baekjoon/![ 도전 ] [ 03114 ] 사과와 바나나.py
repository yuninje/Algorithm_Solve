# https://www.acmicpc.net/problem/3114
# 2 <= R, C <= 1500
#   A : 사과   , B : 바나나
#   1 <= 나무 <= 99
#   B : True      A : False

import sys
I = sys.stdin.readline
R, C = list(map(int, I().split()))

arr = [[[0,0]] * (C+1) for _ in range(0,R+1)]
for r in range(1,R+1):
    line = I().split()
    for c in range(1,C+1):
        if line[c-1][0] == 'B':
            arr[r][c] = [0,int(line[c-1][1:])]            
        else:
            arr[r][c] = [int(line[c-1][1:]),0]
                   
arr[1][1] = [0,0]
arr[R][C] = [0,0]

dp = [[0] * (C+1) for _ in range(0,R+1)]
for r in range(1,R):
    for c in range(2,C+1):
        dp[r][1] += arr[r][c][1]



#  증가
for r in range(1,R):
    for c in range(2, C+1):
        dp[r][c] = dp[r][c-1] - arr[r][c][1] + arr[r][c-1][0]

for c in range(2,C+1):
    dp[R][c] = dp[R][c-1] + arr[R][c-1][0]

print("dp======================================")
for d in dp:
    print(d)

for r in range(1,R+1):
    for c in range(1,C+1):
        dp[r][c] = max(dp[r-1][c], dp[r-1][c-1]) + dp[r][c]
        dp[r][c] = max(dp[r][c] , dp[r][c-1]-arr[r][c][1])


print("result dp ==================================")
for d in dp:
    print(d)


print(dp[R][C])