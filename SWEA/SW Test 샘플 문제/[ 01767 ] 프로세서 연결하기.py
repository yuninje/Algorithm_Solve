# 12:43 ~ 
# 7 <= N <= 12
# 1 <= Core <= 12
# 0 : 빔 , 1 : Core
# 방향 >>  1 : 동  2 : 서  3 : 남  4: 북
def dfs(arr, a1_index, dir, count):
    global answer
    a1_index += 1
    if dir == 1:    # 동    a1[][1]+1 ~ N-1
        for n in range(a1[a1_index][1]+1 , N):  
            if arr[a1[a1_index][0]] [n] != 0:   # 확인
                return
        for n in range(a1[a1_index][1]+1 , N):  
            arr[a1[a1_index][0]] [n] = 2
            count += 1

    elif dir == 2:   # 서   0 ~ a1[][1]-1
        for n in range(0 , a1[a1_index][1]):
            if arr[a1[a1_index][0]] [n] != 0:
                return
        for n in range(0 , a1[a1_index][1]):    
            arr[a1[a1_index][0]] [n] = 2
            count += 1

    elif dir == 3:  # 남    a1[][0]+1 ~ N-1
        for n in range(a1[a1_index][0]+1, N):
            if arr[n] [a1[a1_index][1]] != 0:
                return
        for n in range(a1[a1_index][0]+1, N):
            arr[n] [a1[a1_index][1]] = 2
            count += 1

    elif dir == 4:  # 북    0 ~ a1[][0]-1
        for n in range(0,a1[a1_index][0]):
            if arr[n] [a1[a1_index][1]] != 0:
                return
        for n in range(0,a1[a1_index][0]):
            arr[n] [a1[a1_index][1]] = 2
            count += 1

    if a1_index == len(a1)-1:
        if count < answer:
            answer = count
    else:
            
        # 동
        dfs(arr, a1_index, 1, count)
        # 서
        dfs(arr, a1_index, 2, count)
        # 남
        dfs(arr, a1_index, 3, count)
        # 북
        dfs(arr, a1_index, 4, count)

    if dir == 1:    # 동
        for n in range(a1[a1_index][1]+1 , N):  
            arr[a1[a1_index][0]] [n] = 0
            count -= 1
    elif dir == 2:   # 서
        for n in range(0 , a1[a1_index][1]):    
            arr[a1[a1_index][0]] [n] = 0
            count -= 1
    elif dir == 3:  # 남
        for n in range(a1[a1_index][0]+1, N):
            arr[n] [a1[a1_index][1]] = 0
            count -= 1
    elif dir == 4:  # 북
        for n in range(0,a1[a1_index][0]):
            arr[n] [a1[a1_index][1]] = 0
            count -= 1

T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = []
    for n in range(0,N):
        arr.append(list(map(int,input().split())))

    a1 = []
    for r in range(1,N-1):
        for c in range(1,N-1):
            if arr[r][c] == 1:
                breakCount = 0
                for n in range(0,r):
                    if arr[n][c] == 1:
                        breakCount += 1
                        break
                for n in range(r+1, N):
                    if arr[n][c] == 1:
                        breakCount += 1
                        break
                for n in range(0, c):
                    if arr[r][n] == 1:
                        breakCount += 1
                        break
                for n in range(c+1, N):
                    if arr[r][n] == 1:
                        breakCount += 1
                        break
                if breakCount == 4:
                    # print("r : " + str(r) + "  c : " + str(c))
                    continue
                a1.append([r,c])

    answer = 9223372036
    dfs(arr, -2, 0, 0)
    
    print("#"+str(test) + " " + str(answer))