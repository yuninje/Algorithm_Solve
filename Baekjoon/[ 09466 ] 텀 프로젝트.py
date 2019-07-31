# 2 <= N <= 100,000

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
        bool_arr[dum[-1]]
        while True:
            if arr[dum[-1]] == dum[-1]:
                answer += len(dum)-1
                break
            else:
                if bool_arr[arr[dum[-1]]]:
                    if arr[dum[-1]] in dum:
                        answer += dum.index(arr[dum[-1]])
                    else:
                        answer += len(dum)
                    break
                else:
                    dum.append(arr[dum[-1]])
                    bool_arr[dum[-1]] = True
            
    print(answer)
            
    