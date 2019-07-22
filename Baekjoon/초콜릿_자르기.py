# N * M 초콜릿
# 쪼개는 회수를 최소
# 1 <= N, M <= 300

R, C = list(map(int, input().split()))

dp = []
for r in range(0,R+1):
    dp.append([0 for _ in range(0,C+1)])

dp[1][1] = 0
for r in range(2,R+1):
    dp[r][1] = r-1
for c in range(2,C+1):
    dp[1][c] = c-1
    

for r in range(2,R+1):
    for c in range(2,C+1):
        if r >= c :
            if r % 2 == 0:
                dp[r][c] = dp[int(r/2)][c] * 2 + 1
            else:
                dp[r][c] = dp[int(r/2)][c] + dp[r - int(r/2)][c] +1
        else:
            if c % 2 == 0:
                    dp[r][c] = dp[r][int(c/2)] * 2 + 1
            else:
                dp[r][c] = dp[r][int(c/2)] + dp[r][(c-int(c/2))] +1
                

print(dp[R][C])