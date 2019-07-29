def dfs(visit, r, c,  total, count):
    global answer
    if visit[r][c]:
        return

    visit[r][c] = True 
    total += arr[r][c]
    count +=1 

    if count == 4:
        if total > answer:
            answer = total
        visit[r][c] = False
        return

    if r-2 > 0:
        if visit[r-2][c] and visit[r-1][c] :
            dfs(visit, r-1, c+1, total, count)      # ㅏ 모양          
            dfs(visit, r-1, c-1, total, count)      # ㅓ 모양
    if c-2 > 0:
        if visit[r][c-2] and visit[r][c-1]:
            dfs(visit, r+1, c-1, total, count)      # ㅜ 모양     
            dfs(visit, r-1, c-1, total, count)      # ㅗ 모양


    dfs(visit, r+1, c, total, count)
    # dfs(visit, r-1, c, total, count)    
    dfs(visit, r, c+1, total, count)
    dfs(visit, r, c-1, total, count)
    
    visit[r][c] = False


N, M = list(map(int, input().split()))

arr = [[0 for _ in range(0,M+2)] for _ in range(0,N+2)]
for r in range(1,N+1):
    line = input().split()
    for c in range(1,M+1):
        arr[r][c] = int(line[c-1])

visit = [[True for _ in range(0,M+2)] for __ in range(0,N+2)]
for n in range(1,N+1):
    for m in range(1,M+1):
        arr[n][m] = False

answer = 0
for n in range(1,N+1):
    for m in range(1,M+1):
        dfs(visit, n, m , 0, 0)

print(answer)