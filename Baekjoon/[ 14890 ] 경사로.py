N, L = list(map(int, input().split()))
arr = [[0 for _ in range(0,N+2)] for __ in range(0,N+2)]
for r in range(1,N+1):
    line = input().split()
    for c in range(1,N+1):
        arr[r][c] = int(line[c-1])

answer = 0

for r in range(1,N+1,1):
    jump_c = -1
    breakFlag = False

    before = arr[r][1]
    count = 1

    for c in range(2,N+1,1):
        if c <= jump_c:
            continue

        if before == arr[r][c]-1 :     # before < arr[r][c]   1차이
            if count < L:
                breakFlag = True
                break
            before = arr[r][c]
            count = 1

        elif before == arr[r][c]:       
            count += 1

        elif before-1 == arr[r][c]:    # before > arr[r][c]   1차이
            for i in range(c+1,c+L):    # 뒤에꺼 미리 확인
                if arr[r][c] != arr[r][i]:
                    breakFlag = True
                    break
            if breakFlag:               # 뒤에꺼 불통과
                break
            else:                       # 뒤에꺼 통과
                before = arr[r][c]
                count = 0
                jump_c = c+L-1

        else:                           # before , arr[r][c] 차이 1 초과 
            breakFlag = True
            break
    if not breakFlag:
        # print("answer ---- r : " + str(r))
        answer += 1
        

for c in range(1,N+1,1):
    jump_r = -1
    breakFlag = False

    before = arr[1][c]
    count = 1

    for r in range(2,N+1,1):
        if r <= jump_r:     
            continue

        if before == arr[r][c]-1 :      # before < arr[r][c]   1차이
            if count < L:
                breakFlag = True
                break
            before = arr[r][c]
            count = 1

        elif before == arr[r][c]:       # before == arr[r][c]  같을때 카운트++
            count += 1

        elif before-1 == arr[r][c]:     # before > arr[r][c]    1차이
            for i in range(r+1,r+L):    # 뒤에꺼 미리 확인
                if arr[r][c] != arr[i][c]:
                    breakFlag = True
                    break
            if breakFlag:               # 뒤에꺼 불통과
                break
            else:                       # 뒤에꺼 통과
                before = arr[r][c]
                count = 0
                jump_r = r+L-1

        else:                           # before , arr[r][c]  1초과
            breakFlag = True
            break
    if not breakFlag:
        # print("answer ---- c : " + str(c))
        answer += 1

print(answer)