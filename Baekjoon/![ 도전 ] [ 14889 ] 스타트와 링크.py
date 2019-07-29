# https://www.acmicpc.net/problem/14889
# S[i,j] = a[i] 와 a[j] 의 시너지
# i와 j 가 같은 팀이 될경우 > 능력치 : S[i,j] + S[j,i]
# N <= N <= 20, N : 짝수
#   1 <= S[i,j] <= 100

N = int(input())
S = [[0 for _ in range(0,N)] for __ in range(0,N)]
for i in range(0,N):
    line = input().split()
    for j in range(0,N):
        S[i][j] = int(line[j])

for s in S:
    print(s)

