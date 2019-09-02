# https://www.acmicpc.net/problem/2629
import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = list(map(int, input().split())) # 추
M = int(input())
mrr = list(map(int, input().split())) #  무게를 확인하고자 하는 구슬들
dp = [[False] * 30001 for _ in range(31)]
dp[0][15000] = True
for n in range(1,N+1):
    for d in range(0, 30001):
        if dp[n-1][d]:
            dp[n][d + arr[n-1]] = True
            dp[n][d] = True
            dp[n][d - arr[n-1]] = True 
answer = []
for m in mrr:
    if m <= 15000:
        if dp[N][m+15000]:
            answer.append('Y')
        else:
            answer.append('N')
    else:
        answer.append('N')
print(' '.join(answer))