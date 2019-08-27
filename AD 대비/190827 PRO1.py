# R, C
# 0 ~ 10  ( 11 개 )
#

T = int(input())
for test in range(1,T+1):
    R, C, K = list(map(int, input().split()))
    arr = [list(map(int, input().split()))  for _ in range(0,K)]
    area = [[0] * C for _ in range(0,R)]
    answer = [0] * 11
    answer[0] = R * C
    for a in arr:
        r1 = a[0]
        c1 = a[1]
        r2 = a[2]
        c2 = a[3]
        color = a[4]
        flag = False
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if area[r][c] > color:
                    flag = True
                    break
            if flag:
                break
        if flag:
            continue
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                answer[area[r][c]] -= 1
                answer[color] += 1
                area[r][c] = color
    print('#'+str(test)+ ' ' + str(max(answer)))