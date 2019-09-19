def solution(order):
    dir = [[-2,0], [2,0], [0,2], [0,-2]] # U, D, R, L
    answer = 0
    
    N = 10
    MAX_N = 2 * N + 1
    nowX = N
    nowY = N
    cMap = [[0] * (MAX_N) for _ in range(MAX_N)]
    for o in order:
        if o == 'U':
            d = 0
        elif o == 'D':
            d = 1
        elif o == 'R':
            d = 2
        else:
            d = 3
        dx = dir[d][0]
        dy = dir[d][1]
        
        if 0 <= nowX + dx and nowX + dx < MAX_N and 0 <= nowY + dy and nowY + dy < MAX_N:
            cMap[nowX + dx//2][nowY + dy//2] = 1
            nowX += dx
            nowY += dy
    
    for r in cMap:
        for c in r:
            if c == 1:
                answer += 1
        
    return answer