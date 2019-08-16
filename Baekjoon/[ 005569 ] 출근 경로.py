# https://www.acmicpc.net/problem/5569

C, R= list(map(int, input().split()))

arr = [[0] * (2 * C) for _ in range(0,2*R)]

for r in range(0,2 * R):
    arr[r][1] = 1
for c in range(0,2 * C):
    arr[1][c] = 1
    

for r in range(2,2*R):
    for c in range(2,2*C):        
        if r % 2 == 1 and c % 2 == 0: # 가로
            arr[r][c] = arr[r][c-2] + arr[r-3][c-1]
        elif r % 2 == 0 and c % 2 == 1 : # 세로
            arr[r][c] = arr[r-2][c] + arr[r-1][c-3]



# for a in arr:
#     print(a)


print((arr[2*R-2][2 * C-1]+arr[2 * R - 1][2 * C-2]) % 100000)