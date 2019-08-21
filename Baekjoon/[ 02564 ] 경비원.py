# https://www.acmicpc.net/problem/2564
# 1 <= R, C <= 100
# 1 : 북 , 2 : 남, 3 : 서, 4 : 동

C,R = list(map(int, input().split()))
N = int(input())
shop_real = []
shop = []
for n in range(0,N+1):
    a = list(map(int, input().split()))
    shop.append(a)
    if a[0] == 1:
        shop_real.append([0,a[1]])
    elif a[0] == 2:
        shop_real.append([R, a[1]])
    elif a[0] == 3:
        shop_real.append([a[1], 0])
    elif a[0] == 4:
        shop_real.append([a[1], C])

result = 0
for n in range(0,N):
    if shop[n][0] == shop[N][0]: # 같은줄
        plus = abs(shop[n][1] - shop[N][1])
    elif (shop[n][0]-1)//2 == (shop[N][0]-1)//2: # 건너편 줄
        if shop[n][0] == 1 or shop[n][0] == 2:
            plus = min(2*C - (shop[n][1]+shop[N][1]), shop[n][1]+shop[N][1])+R
        else:
            plus = min(2*R - (shop[n][0]+shop[N][0]), shop[n][0]+shop[N][0])+C
    else:
        plus = abs(shop_real[n][0] - shop_real[N][0]) + abs(shop_real[n][1] - shop_real[N][1])
    result += plus
print(result)
