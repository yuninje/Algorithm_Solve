# https://www.acmicpc.net/problem/2635
def dfs(r, c):
    if c < r-c:
        return 3
    elif c == r-c:
        return 5
    elif c - (r-c) > r-c:
        return 4
    else:
        return dfs(c,r-c)+1

N = int(input())
MAX = 0
MAX_IDX = -1
for c in range(N//2 , N+1):
    result = dfs(N,c)
    if MAX < result:
        MAX = result
        MAX_IDX = c

print(MAX)
arr = [N, MAX_IDX]
while arr[-2] >= arr[-1]:
    arr.append(arr[-2]-arr[-1])
print(' '.join(list(map(str, arr))))