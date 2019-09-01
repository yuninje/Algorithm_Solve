 # https://www.acmicpc.net/problem/2669
 # 1 <= x, y <= 100

arr = [list(map(int, input().split())) for _ in range(4)]

R = 10
area = [[False] * R for _ in range(R)]
answer = 0
for a in arr:
    for r in range(a[0], a[2]):
        for c in range(a[1], a[3]):
            if area[r][c] == False:
                area[r][c] = True
                answer += 1

print(answer)