# https://www.acmicpc.net/problem/1520
# 1 <= R, C <= 500
# 1 <= arr[r][c] <= 10000

def dfs(r, c):
    global answer
    if r == R-1 and c == C-1:
        answer += 1

    for d in dir:
        if R > r+d[0] and r+d[0] >= 0 and C > c + d[1] and c + d[1] >= 0 and arr[r][c] > arr[r+d[0]][c+d[1]]: 
            dfs(r+d[0],c+d[1])
            
dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, input().split()))
arr = []
for r in range(0,R):
    arr.append(list(map(int, input().split())))
answer = 0
dfs(0,0)
print(answer)