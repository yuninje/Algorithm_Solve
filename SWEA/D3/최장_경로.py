# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB
def dfs(visit, now):
  global count
  visit[now] = True
  if count < sum(visit):
    count = sum(visit)
  for i in range(0, M):
    if line[i][0] == now and not visit[line[i][1]] :
      dfs(visit.copy(), line[i][1])
    
    if line[i][1] == now and not visit[line[i][0]] :
      dfs(visit.copy(), line[i][0])

T = int(input())
answer = []
for i in range(0,T):
  N, M = map(int, input().split( ))
  line = [ ]
  for l in range(0,M):
    l_1, l_2 = map(int, input().split( ))
    line.append([l_1, l_2])

  visit = [False for _ in range(N+1)]
  line = sorted(line, key = lambda x : (x[0],x[1]))
  count = 0
  for j in range(1, N+1):
    dfs(visit.copy(), j)

  answer.append(count)

for i in range(0,len(answer)):
    print("#"+str(i+1) +" "+ str(answer[i]))
    