def find(nr,nc):
    global answer
    left = nc
    right = N - 1 - nc

    for l in range(left,0,-1):
        for r in range(right,0,-1):
            # print('nr : ' + str(nr) + '  nc : ' + str(nc) + '  left : ' + str(l) + '  right : ' + str(r))
            if check(nr, nc, l, r):
                # print('check : true')
                answer = max((l+1) * 2 + (r+1) * 2 - 4, answer)
                
def check(sr, sc, left, right):
    if left + right + sr >= N:
        return False
    r, c = sr, sc
    li = set()
    li.add(Map[r][c])
    for _ in range(left):
        r += 1
        c -= 1
        if Map[r][c] in li:
            return False
        li.add(Map[r][c])
    
    for _ in range(right):
        r += 1
        c += 1
        if Map[r][c] in li:
            return False
        li.add(Map[r][c])

    for _ in range(left):
        r -= 1
        c += 1
        if Map[r][c] in li:
            return False
        li.add(Map[r][c])

    for _ in range(right-1):
        r -= 1
        c -= 1
        if Map[r][c] in li:
            return False
        li.add(Map[r][c])
    return True

T = int(input())
dir = [[1,1],[1,-1],[-1,1],[-1,-1]]
for test in range(1,T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]    
    answer = -1

    # solution
    for r in range(N):
        for c in range(N):
            find(r,c)


    print('#' + str(test) + ' ' + str(answer))