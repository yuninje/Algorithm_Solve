# https://www.acmicpc.net/problem/1261
# 1 <= N, M <= 100
import sys
I = sys.stdin.readline

def bfs():
    que = [(0,0)]
    # 현재 방 구하기
    visit = [[False] * C for _ in range(R)]
    visit[0][0] = True
    count = 0

    while True:
        qque = []
        while que:
            que_ = []
            for r, c in que:
                if r == R-1 and c == C-1:
                    return count

                for dr, dc in dir:
                    rr, cc = r + dr, c + dc
                    if not ( 0 <= rr < R and 0 <= cc < C) or visit[rr][cc]:
                        continue
                    if Map[rr][cc] == 0:
                        que_.append((rr,cc))
                        visit[rr][cc] = True
            qque += que
            que = que_
        
        # 새로운 방

        que = qque
        print(que)
        que_ = []
        for r, c in que:
            if r == R-1 and c == C-1:
                return count

            for dr, dc in dir:
                rr, cc = r + dr, c + dc
                if not ( 0 <= rr < R and 0 <= cc < C) or visit[rr][cc]:
                    continue
                if visit[rr][cc]:
                    continue
                if Map[rr][cc] == 1:
                    visit[rr][cc] = True
                    que_.append((rr,cc))
        que = que_
        count += 1


C,R = map(int, I().split())
Map = [list(input()) for _ in range(R)]
dir = [[1,0],[0,1],[-1,0],[0,-1]]
print(bfs())