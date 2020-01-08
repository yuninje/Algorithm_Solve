# https://www.acmicpc.net/problem/1014

def existDot(Map, R, C):
    for r in range(R):
        for c in range(C):
            if Map[r][c] == '.':
                return True
    return False

T = int(input())
answer = [0] * T
for t in range(T):
    R, C= map(int, input().split())
    Map = [list(input()) for _ in range(R)]
    while existDot(Map, R, C):
    # if True:
        arr = [0] * C
        for c in range(C):
            count = 0
            for r in range(R):
                if Map[r][c] == '.':
                    count += 1
            arr[c] = count

        dp = [0] * C
        dpA = [False] * C
        dpB = [False] * C
        dp[0] = arr[0]
        dpB[0]= True

        for c in range(1,C):
            dpA = dpB
            if dp[c-1] >= dp[c-2] + arr[c]:
                dp[c] = dp[c-1]
                for cc in range(c):
                    dpB[cc] = dpA[cc]
            else:
                dp[c] = dp[c-2] + arr[c]
                dpB[c] = True

        answer[t] += dp[-1]

        for c in range(C):
            if dpB[c]:
                for r in range(R):
                    if Map[r][c] == '.':
                        Map[r][c] = 'x'
                        if 0 <= c-1:
                            Map[r][c-1] = 'x'
                            if r+1 < R:
                                Map[r+1][c-1] = 'x'
                        if c+1 < C:
                            Map[r][c+1] = 'x'
                            if r+1 < R:
                                Map[r+1][c+1] = 'x'
for a in answer:
    print(a)