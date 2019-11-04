def dfs(r, color, total):
    global answer
    total += C - count[r][color] 
    
    if total > answer:
        return
    # print('r : ' + str(r) + '  color : ' + str(color) + '  total : ' + str(total))
    if r == 0:
        dfs(r+1, 0, total)
        dfs(r+1, 1, total)
    elif r < R-1:
        if color == 0:
            dfs(r+1, 0, total)
            dfs(r+1, 1, total)
        elif color == 1:
            dfs(r+1, 1, total)
            dfs(r+1, 2, total)
        else:
            dfs(r+1, 2, total)
    else: # r == R-1
        if color != 2:
            return
        answer = min(answer, total)
    
T = int(input())
for test in range(1,T+1):
    R, C = list(map(int, input().split()))
    arr = [list(input()) for _ in range(R)]
    count = [[0,0,0] for _ in range(R)]
    # W, B,  R
    for n in range(R):
        for a in arr[n]:
            if a == 'W':
                count[n][0] += 1
            elif a == 'B':
                count[n][1] += 1
            else:
                count[n][2] += 1
    answer = 9999999999
    dfs(0,0,0)
    print('#' + str(test) + ' ' + str(answer))