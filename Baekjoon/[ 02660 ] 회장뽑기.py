# https://www.acmicpc.net/problem/2660

def bfs(n):
    visit = [False] * (N+1)
    visit[n] = True
    queue = [n]
    count = 1
    total = 0
    while queue:
        queue_ = []
        for q in queue:
            for i in range(1, N+1):
                if visit[i] or not inner[q][i]:
                    continue
                visit[i] = True
                total += 1
                queue_.append(i)
        if total == N-1:
            return count
        queue = queue_
        count += 1

    return count


N = int(input())
arr = []
while True:
    a = list(map(int, input().split()))
    if a[0] == -1:
        break
    arr.append(a)
inner = [[False] * (N+1) for _ in range(N+1)]
for a in arr:
    inner[a[0]][a[1]] = True
    inner[a[1]][a[0]] = True
MIN = 999999
ANSWER = [-1]
for n in range(1,N+1):
    b = bfs(n)
    if MIN > b:
        MIN = b
        ANSWER = [n]
    elif MIN == b:
        ANSWER.append(n)
print(str(MIN) + ' ' + str(len(ANSWER)))
print(' '.join(map(str, ANSWER)))