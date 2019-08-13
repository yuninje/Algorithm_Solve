# https://www.acmicpc.net/problem/2644

def bfs():
    queue = arr[X]
    count = 1
    while queue:
        queue_ = []
        for q in queue:
            if q == Y:
                return count
            for a in arr[q]:
                if not visit[a]:
                    visit[a] = True
                    queue_.append(a)
        queue = queue_
        count += 1
    return -1

N = int(input())
X, Y = list(map(int, input().split()))
M = int(input())
arr = [[] for _ in range(0,N+1)] 
for m in range(0,M):
    line = list(map(int,input().split()))
    arr[line[0]].append(line[1])
    arr[line[1]].append(line[0])
visit = [0] * (N+1)

print(bfs())