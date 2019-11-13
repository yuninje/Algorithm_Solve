# https://www.acmicpc.net/problem/2239
def dfs(r,c):
    for rr in range(r,N):
        for cc in range(N):
            if Map[rr][cc] == 0:
                arr = check(rr,cc)
                for i in range(1,N+1):
                    if arr[i]:
                        Map[rr][cc] = i
                        if dfs(rr,cc):
                            return True
                Map[rr][cc] = 0
                return False
    return True


def check(r,c):
    arr = [True] * (N+1)
    for rr in range(N):
        arr[Map[rr][c]] = False
    for cc in range(N):
        arr[Map[r][cc]] = False
    
    for rr in range(3 * (r // 3) , 3 * (r // 3) + 3):
        for cc in range(3 * (c // 3) , 3 * (c // 3 ) + 3):
            arr[Map[rr][cc]] = False
    
    return arr
N = 9
Map = [list(map(int, list(input()))) for _ in range(N)]
dfs(0,0)
for m in Map:
    print(''.join(list(map(str,m))))