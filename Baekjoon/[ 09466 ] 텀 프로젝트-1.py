T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    bool_arr = [False for _ in range(0,N+1)]

    answer = 0
    for n in range(1,N+1): 
        if bool_arr[n]:
            continue
        dum = [n]
        bool_arr[n] = True
        breakFlag = False
        while True:
            for di in range(len(dum)-1,-1,-1):
                if arr[dum[-1]] == dum[di]:
                    answer += di
                    breakFlag = True
                    break
            if breakFlag:
                break

            if bool_arr[arr[dum[-1]]]:
                answer += len(dum)
                break

            dum.append(arr[dum[-1]])
            bool_arr[dum[-1]] = True
    print(answer)