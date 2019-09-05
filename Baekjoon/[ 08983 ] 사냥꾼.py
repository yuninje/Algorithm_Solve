# https://www.acmicpc.net/problem/8983
# 1 <= M (사대(총을 쏘는 장소)의 수) <= 100,000
# 1 <= N (동물의 수) <= 100,000
# 1 <= L (사정거리) <= 1,000,000,000

M, N, L = list(map(int, input().split()))
srr = list(map(int, input().split()))
animal = [list(map(int, input().split())) for _ in range(N)]

srr = sorted(srr)
animal = sorted(animal, key=lambda x: (x[0],x[1]))


plusFlag = False
idx = 0
answer = 0
for c,r in animal:
    # print(' c , r : ' + str(c) + ' ' + str(r))
    while True:
        if idx == N:
            break
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
                if plusFlag:
                    idx -= 1
                    break


        else:       # idx 보다 오른쪽
            if abs(d) <= L:  # c 사정거리 내
                if abs(d) + r <= L: # 사냥 가능
                    # print('사냥 가능 c , r : ' + str(c) + ' ' + str(r) )
                    answer += 1
                    break
                else:               #
                    # idx 더해서 해보고 되면 유지 안되면 idx 빽업
                    if idx == N-1:
                        break
                    if abs(c - srr[idx]) > abs(c-srr[idx+1])
                        idx += 1
            else: # 사정거리 밖.
                if idx == N-1:
                    idx ++
                    break
                idx += 1
print(answer)




