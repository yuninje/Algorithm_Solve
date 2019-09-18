# https://www.acmicpc.net/problem/8983
# 1 <= M (사대(총을 쏘는 장소)의 수) <= 100,000
# 1 <= N (동물의 수) <= 100,000
# 1 <= L (사정거리) <= 1,000,000,000
import sys
I = sys.stdin.readline
M, N, L = list(map(int, I ().split()))
srr = list(map(int, I ().split()))
animal = [list(map(int, I ().split())) for _ in range(N)]

srr = sorted(srr)
animal = sorted(animal, key=lambda x: (x[0],x[1]))
endFlag = False
idx = 0
answer = 0
for c,r in animal:
    # print(' c , r : ' + str(c) + ' ' + str(r))

    while True:
        d = c - srr[idx]
        if d < 0:  # idx  보다 왼쪽
            if abs(d) <= L:  # c 사정거리 내
                if abs(d) + r <= L: # 사냥 가능
                    # print('good ! c , r : ' + str(c) + ' ' + str(r) )
                    answer += 1
                    break
                else:               # 사냥 불가능
                    break
            else:            # 사정거리 밖
                break

        else:       # idx 보다 오른쪽
            if abs(d) <= L:  # c 사정거리 내
                if abs(d) + r <= L: # 사냥 가능
                    # print(str(r) + ', ' + str(c))
                    answer += 1
                    break
                else:           # 사냥 불가
                    if idx == M - 1:
                        break
                    if abs(c-srr[idx]) >= abs(c-srr[idx+1]):   # 다음 idx 가 더 가까우면
                        idx += 1
                    else:
                        break
            else: # 사정거리 밖.
                if idx == M-1:
                    endFlag = True
                    break
                idx += 1
    if endFlag:
        break
print(answer)