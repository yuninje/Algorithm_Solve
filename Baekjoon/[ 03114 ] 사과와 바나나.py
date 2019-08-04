# https://www.acmicpc.net/problem/3114
# 2 <= R, C <= 1500
#   A : 사과   , B : 바나나
#   1 <= 나무 <= 99
#   B : True      A : False

import sys
I = sys.stdin.readline
R, C = list(map(int, I().split()))

arr = [[[0,0]] * (C+1) for _ in range(0,R+1)]   # [A,B]로 저장. B1 일 경우 [0,1], A6 일 경우 [6,0]

for r in range(1,R+1):
    line = I().split()
    for c in range(1,C+1):
        if line[c-1][0] == 'B':
            arr[r][c] = [0,int(line[c-1][1:])]  # 두자리 수로 인하여 [1:] 사용 
        else:
            arr[r][c] = [int(line[c-1][1:]),0]

for c in range(1,C+1):
    arr[1][c][0] = 0            # 첫번재 줄의 A들은 어짜피 적용이 안된다.
    arr[R][c][1] = 0            # 마지막 줄의 B들은 어짜피 적용이 안된다.


dp = [[0] * (C+1) for _ in range(0,R+1)]  # dp 선언

for r in range(1,R+1):
    for c in range(2,C+1):
        dp[r][1] += arr[r][c][1]        # 필요없는 연산을 줄이기위해 dp[r][1] 의 값을 먼저 계산. ( 이후엔 이 값을 바탕으로 계산)

#  dp 초기화
for r in range(1,R+1):
    for c in range(2, C+1):
        dp[r][c] = dp[r][c-1] - arr[r][c][1] + arr[r][c-1][0]   # dp 초기값들은 해당 지점에 불도저가 지나갔을 때 해당 row 의 열매 증가값.

for r in range(1,R+1):
    if r != 1 :
        dp[r][1] += dp[r-1][1]
    for c in range(2,C+1):
        dp[r][c] = max(dp[r-1][c], dp[r-1][c-1]) + dp[r][c]
        dp[r][c] = max(dp[r][c] , dp[r][c-1]-arr[r][c][1])

print(dp[R][C])