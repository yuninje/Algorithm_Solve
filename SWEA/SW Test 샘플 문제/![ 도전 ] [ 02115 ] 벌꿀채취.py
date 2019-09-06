# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu
# N ; 벌통들의 크기    3 <= N <= 10
# M : 벌통의 개수       M <= N
# C : 굴을 채취할 수 있는 최대 양   10 <= C <= 30
T = int(input())
for test in range(1, T+1):
    N, M, C = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    \
    