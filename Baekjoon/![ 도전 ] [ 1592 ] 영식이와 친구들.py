# https://www.acmicpc.net/problem/1592
# 3 <= N ( 사람 수 ) <= 1000
# 1 <= M ( 최대 공 받는 횟수 )<= 1000
# L ( L번째 사람에게 던지기 )< N
# 공받은 횟수가  홀수 > 시계방향 L
#               짝수 > 반시계방향 L

N, M, L = list(map(int, input().split()))
arr = [0] * (N)
idx = 1
answer = 0
while True:
    arr[idx] += 1
    if arr[idx] == M:
        break
    answer += 1
    if arr[idx] % 2 == 0: # 짝수 > 반시계 방향 L
        idx -= L
        idx %= N
    else:
        idx += L
        idx %= N
print(answer)

