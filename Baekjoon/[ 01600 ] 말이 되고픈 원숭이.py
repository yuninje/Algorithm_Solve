# https://www.acmicpc.net/problem/1600
import sys
I = sys.stdin.readline
def bfs():
    global answer
    # r, c, horse_count
    que = [(0,0,K)]
    visit[K][0][0] = True
    count = 0
    while que:
        que_ = []
        for r, c, k in que:
            if r == R-1 and c == C-1:
                return count
            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not (0 <= rr < R and 0 <= cc < C) or Map[rr][cc] == 1 or visit[k][rr][cc]:
                    continue
                visit[k][rr][cc] = True
                que_.append((rr,cc,k))

            if k > 0:
                for hdr, hdc in horse_dir:
                    rr, cc = r + hdr, c + hdc
                    if not ( 0 <= rr < R and 0 <= cc < C )  or Map[rr][cc] == 1 or visit[k-1][rr][cc]:
                        continue
                    visit[k-1][rr][cc] = True
                    que_.append((rr,cc,k-1))
            
        que = que_
        count += 1

    return -1


dir = [[1,0], [-1,0], [0,1], [0,-1]]
horse_dir = [[-1,-2], [-1,2],[1,2],[1,-2],[-2,1],[-2,-1],[2,1],[2,-1]]
K = int(I())
C, R = list(map(int, I().split()))
Map = [list(map(int, I().split())) for _ in range(R)]
visit = [[[False] * C for _ in range(R)] for __ in range(K+1)]

answer = bfs()

print(answer)