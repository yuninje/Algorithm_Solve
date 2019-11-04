def action(order):
    move(order)

    if order == 'down' or order == 'up':
        for r in range(N-1):
            for c in range(N):
                if Map[r][c] == Map[r+1][c]:
                    Map[r][c] *= 2
                    Map[r+1][c] = 0
    elif order == 'left' or order == 'right':
        for r in range(N):
            for c in range(N-1):
                if Map[r][c] == Map[r][c+1]:
                    Map[r][c] *= 2
                    Map[r][c+1] = 0
        
    move(order)

def move(order):
    if order == 'down':
        for r in range(N-1, -1, -1):
            for c in range(N):
                if Map[r][c] == 0:
                    for rr in range(r, 0, -1):
                        Map[rr][c] = Map[rr-1][c]
                    Map[0][c] = 0
                    c += 1
    elif order == 'up':
        for r in range(N):
            for c in range(N):
                if Map[r][c] == 0:
                    for rr in range(r, N-1):
                        Map[rr][c] = Map[rr+1][c]
                    Map[N-1][c] = 0
                    c -= 1
    elif order == 'left':
        for r in range(N):
            for c in range(N):
                if Map[r][c] == 0:
                    for cc in range(c, N-1):
                        Map[r][cc] = Map[r][cc+1]
                    Map[r][N-1] = 0
                    c -= 1
    else:
        for r in range(N):
            for c in range(N-1,-1,-1):
                if Map[r][c] == 0:
                    for cc in range(cc, 0, -1):
                        Map[r][cc] = Map[r][cc-1]
                    Map[r][0] = 0 
                    c -= 1                   

T = int(input())
# T = 1
for test in range(1,T+1):
    N, order = input().split()
    N = int(N)
    Map = [list(map(int, input().split())) for _ in range(N)]

    # N, order = 20, 'up'
    # Map = [[1] * N for _ in range(N)]
    action(order)
    
    print('#' + str(test))
    for m in Map:
        print(' '.join(list(map(str, m))))

