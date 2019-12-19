# https://www.acmicpc.net/problem/10835
# 왼쪽만, 같이 버릴경우 점수 X
# L < R 이면 R 버릴 수 있다. 점수 O
# 1 <= N <= 2,000
# 1 <= A <= 2,000
# 1 <= B <= 2,000
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline
def dfs(l, r):
    if l == N or r == N:
        return 0

    if dp[l][r] == -1:
        if left[l] > right[r]:
            dp[l][r] = dfs(l, r+1) + right[r]
        else:
            dp[l][r] = max(dfs(l+1,r), dfs(l+1,r+1)) 
    return dp[l][r]

N = int(I())
left = list(map(int, I().split()))
right = list(map(int, I().split()))
dp = [[-1] * N for _ in range(N)]
answer = dfs(0,0)
print(answer)
