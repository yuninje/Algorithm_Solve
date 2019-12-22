# https://www.acmicpc.net/problem/1018
# 8 <= N , M <= 50

R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
N = 8
MIN = 999999999
for rr in range(R-N+1):
    for cc in range(C-N+1):
        # 시작점
        w , b = 0,0
        for r in range(rr,rr + N):
            for c in range(cc, cc+N):
                if (r + c) % 2 == 0:
                    if Map[r][c] == 'W':
                        w += 1
                else:
                    if Map[r][c] == 'B':
                        b += 1
        cal = w + b
        MIN = min(MIN, cal, N*N - cal)
print(MIN)