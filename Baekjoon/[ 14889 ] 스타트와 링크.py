# https://www.acmicpc.net/problem/14889
# S[i,j] = a[i] 와 a[j] 의 시너지
# i와 j 가 같은 팀이 될경우 > 능력치 : S[i,j] + S[j,i]
# N <= N <= 20, N : 짝수
#   1 <= S[i,j] <= 100

def dfs(team_a, count, now):
        if count == N//2:
                team_a.append(-1) # 오류 안나게
                a_index = 0
                team_b = []
                for n in range(0,N):
                        if n != team_a[a_index]:
                                team_b.append(n)
                        else:
                                a_index += 1
                del team_a[-1] # 오류 안나게 제거
                # print("team_a : " + str(team_a))
                # print("team_b : " + str(team_b))
                calculate(team_a, team_b)

        for n in range(now+1,N):
                team_a.append(n)
                dfs(team_a, count+1, n)
                del team_a[-1]
        

def calculate(team_a, team_b):
        global answer
        total_a = 0
        total_b = 0
        result = 0
        for n in range(0,N//2):
                for m in range(0,N//2):
                        total_a += S[team_a[n]][team_a[m]]
                        total_b += S[team_b[n]][team_b[m]]
        
        if total_a > total_b:
                result = total_a - total_b
        else:
                result = total_b - total_a

        if answer > result:
                answer = result

N = int(input())
S = [[0 for _ in range(0,N)] for __ in range(0,N)]
for i in range(0,N):
    line = input().split()
    for j in range(0,N):
        S[i][j] = int(line[j])

# for s in S:
#     print(s)

answer = 9223372036854775807 # python 에서 가질수 있는 최대값
dfs([],0,0)

print(answer)