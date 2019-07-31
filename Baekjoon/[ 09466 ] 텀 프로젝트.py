# https://www.acmicpc.net/problem/9466
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
        bool_arr[dum[-1]] = True
        while True:
            if arr[dum[-1]] == dum[-1]:     # 자기 자신을 가르키고있을때
                answer += len(dum)-1
                break
            else:
                if bool_arr[arr[dum[-1]]]:  # dum의 마지막 숫자가 가르키는 대상이 이미 사용한 숫자일때
                    if arr[dum[-1]] in dum: # 이번에 사용했을 때
                        answer += dum.index(arr[dum[-1]])
                    else:                   # 이전에 이미 사용했을 때
                        answer += len(dum)
                    break
                else:                       # 사용하지 않은 숫자일 때
                    dum.append(arr[dum[-1]])    # dum에 추가
                    bool_arr[dum[-1]] = True
            
    print(answer)
            
    