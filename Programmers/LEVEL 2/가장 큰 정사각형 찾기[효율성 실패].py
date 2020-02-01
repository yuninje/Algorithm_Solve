def solution(board):
    R = len(board)
    C = len(board[0])
    
    answer = 0
    for r in range(R-1, -1, -1):
        if r < answer:
            break
        for c in range(C-1, -1, -1):
            if c <
            if board[r][c] == 0 : continue
            a = 1
            breakFlag = False
            while r + a < R and c + a < C:
                for rr in range(r, r+a+1):
                    if board[rr][c+a] == 1:
                        continue
                    breakFlag = True
                    break
                for cc in range(c, c+a+1):
                    if board[r+a][cc] == 1:
                        continue
                    breakFlag = True
                    break
                if breakFlag:
                    break
                a += 1
            answer = max(answer, a)
                    
    
    return answer * answer