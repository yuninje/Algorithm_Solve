# https://www.acmicpc.net/problem/17837
# 4 <= N ( 체스판의 크기 ) <= 12
# 4 <= K ( 말의 개수 ) <= 10
# 0 : 흰색, 1 : 빨강 , 2 : 파랑
# 0 : 우
# 1 : 상
# 2 : 좌
# 3 : 하

dir = [[0,1], [-1,0], [0,-1], [1,0]]
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
horses = [list(map(lambda x : int(x) - 1 , input().split())) for _ in range(K)]
for horse in horses:
    if horse[2] == 1:
        horse[2] = 2
    elif horse[2] == 2:
        horse[2] = 1

MMap = [[[] for __ in range(N)] for _ in range(N)]
for i in range(K):
    r, c, d = horses[i]
    MMap[r][c] += [i]

answer = 0
flag = False
while answer <= 3:
    print('===============')
    for m in MMap:
        print(m)
    answer += 1
    for i in range(K):
        h = horses[i]
        r, c = h[0], h[1]
        dr, dc = dir[h[2]]
        rr, cc = h[0] + dr, h[1] + dc
        if 0 <= rr < N and 0 <= cc < N :    
            if Map[rr][cc] == 0:
                # 흰
                mm = MMap[r][c]
                for j in range(len(mm)):
                    if mm[j] == i:
                        MMap[rr][cc] += mm[j:]
                        MMap[r][c] = mm[:j]
                        break
                
                if len(MMap[rr][cc]) >=4:
                    flag = True    
                    break 
                continue
            elif Map[rr][cc] == 1:
                # 빨강
                mm = MMap[r][c]
                for j in range(len(mm)):
                    if mm[j] == i:
                        MMap[rr][cc] += reversed(mm[j:])
                        MMap[r][c] = mm[:j]
                        break
                
                if len(MMap[rr][cc]) >=4:
                    flag = True    
                    break
                continue
        # 파랑
        h[2] = ( h[2] + 2 ) % 4
        dr, dc = dir[h[2]]
        rr, cc = h[0] + dr, h[1] + dc
        if 0 <= rr < N and 0 <= cc < N :    
            if Map[rr][cc] == 0:
                # 흰
                mm = MMap[r][c]
                for j in range(len(mm)):
                    if mm[j] == i:
                        MMap[rr][cc] += mm[j:]
                        MMap[r][c] = mm[:j]
                        break
                
                if len(MMap[rr][cc]) >=4:
                    flag = True    
                    break
            elif Map[rr][cc] == 1:
                # 빨강
                mm = MMap[r][c]
                for j in range(len(mm)):
                    if mm[j] == i:
                        MMap[rr][cc] += reversed(mm[j:])
                        MMap[r][c] = mm[:j]
                        break
                
                if len(MMap[rr][cc]) >=4:
                    flag = True    
                    break
    if flag:
        break
            

if(answer > 1000):
    print(-1)
else:
    print(answer)