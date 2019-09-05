# https://www.acmicpc.net/problem/3109

def dfs(r,c):
    global answer
    global flag
    if c == C-1:
        answer += 1
        flag = True
        return

    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if R > rr and rr >= 0 and C > cc and cc >= 0 and arr[rr][cc] == '.':
            arr[rr][cc] = 'x'
            dfs(rr,cc)
            if flag:
                return

dir = [[-1,1],[0,1],[1,1]]
R, C = list(map(int, input().split()))
arr = [list(input()) for _ in range(R)]
answer = 0
for r in range(R):
    flag = False
    dfs(r,0)
print(answer)