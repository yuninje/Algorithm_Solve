# https://www.acmicpc.net/problem/2606

def dfs(start):
    if visit[start]:
        return
    visit[start] = True
    for a in arr[start]:
        dfs(a)

N = int(input())
L  = int(input())
line = []
arr = [[] for _ in range(0,N+1)]
for l in range(0,L):
    line.append(list(map(int, input().split())))
    arr[line[l][0]].append(line[l][1])
    arr[line[l][1]].append(line[l][0])

visit = [False] * (N+1)

dfs(1)
print(sum(visit)-1)