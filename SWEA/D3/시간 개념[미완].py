def solution(now, pro):
    if int(now) > int(pro):
        now = str(int(now) + 240000)
        print(now)
        print(pro)

    else:
        print(now)
        print(pro)
        

    return


T = int(input())

for test in range(1, T+1):
    now = input().replace(':','')
    pro = input().replace(':','')
     
    print(solution(now, pro))
