# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE

def dfs(r, c, count, num):

    if count == K-1:
        setA.add(num)
        return 

    num *= 10
    for dr, dc in dir:
        rr = r + dr
        cc = c + dc
        if 0 <= rr < N and 0 <= cc < N:
            dfs(rr,cc,count+1, num + Map[rr][cc])

dir = [(1,0), (-1,0), (0,1), (0,-1)]
T = int(input())
N = 4
K = 7
for test in range(1,T+1):
    Map = [list(map(int, input().split())) for _ in range(N)]

    setA = set()

    for r in range(N):
        for c in range(N):
            dfs(r,c,0, Map[r][c])

    print('#' + str(test) + ' ' + str(len(setA)))