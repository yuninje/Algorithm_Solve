# https://www.acmicpc.net/problem/3985
# L미터의 롤 케이크
# N명에게 나누어줌
# 1미터 단위로 잘라놓았다.
# 1, 2, 3, ... , L
# 방청객은 1 ~ N
# 원하는 조각을 적는다.
# P와 K를 적어서 내며, P~K 를 원한다는 뜻
# 가장 많은 범위를 적은 방청객, 실제 많이 받은 방청객
# 1 <= L <= 1000
# 1 <= P(i) <= K(i) <= L
L = int(input()) # 롤케익 길이
N = int(input()) # 사람
arr = [list(map(int, input().split())) for _ in range(0,N)]
area = [False] * (L+1)
MAX = -1
MAX_IDX = -1
LONG = -1
LONG_IDX = -1
for a in range(0,N):
    p = 0
    for i in range(arr[a][0], arr[a][1]+1):
        if area[i]:
            continue
        area[i] = True
        p += 1
    if MAX < p:
        MAX = p
        MAX_IDX = a+1
    if arr[a][1] - arr[a][0] > LONG:
        LONG = arr[a][1] - arr[a][0]
        LONG_IDX = a+1

print(LONG_IDX)
print(MAX_IDX)


