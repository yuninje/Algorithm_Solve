# https://www.acmicpc.net/problem/1002
# -10,000 <= x1, y1, x2, y2 <= 10,000
# 0 <= r1, r2 <= 10,000
T = int(input())
for test in range(1,T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 ) ** 0.5
    rr1, rr2 = min(r1, r2), max(r1,r2)
    if d > rr1 + rr2:   # 멀리 떨어져서 만나지 않음
        print(0)
    elif d == rr1 + rr2: # 외접
        print(1)
    elif d < rr1 + rr2:     
        if d == 0:
            if rr1 == rr2:  # 동일한 원
                print(-1)
            else:
                print(0)    # 중심이 같은 다른 원
        else:
            if d == rr2 - rr1:  # 내접 
                print(1)
            elif d < rr2 - rr1: 
                print(0)
            elif d > rr2 - rr1:
                print(2)


            
