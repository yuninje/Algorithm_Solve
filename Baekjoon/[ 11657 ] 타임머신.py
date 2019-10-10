# https://www.acmicpc.net/problem/11657
# 1 <= N <= 500
# 1 <= M <= 6000
# 1 <= A, B <= N, -10000 <= C <= 10000

N, M = list(map(int, input().split()))
buses = [list(map(int, input().split())) for _ in range(M)]
inner = [[999999999] * (N+1) for _ in range(N+1)]
for start, end, value in buses:
    inner[start][end] = value

dist = [999999999] * (N+1)
dist[1] = 0

for _ in range(N-1):
    for start, end, value in buses:
        if dist[start] != 999999999:
            dist[end] = min(dist[end], dist[start] + value)



if N == 1:
    answer = [0]
else:
    for start, end, value in buses:
        if dist[start] != 999999999:
            if dist[end] > dist[start] + value:
                answer = [-1]
                break
    else:
        answer = dist
        del answer[0]
        del answer[0]

        for i in range(len(answer)):
            if answer[i] == 999999999:
                answer[i] = -1

for a in answer:
    print(a)

