# https://www.acmicpc.net/problem/1389
# 2 <= N (유저의 수) <= 100
# 1 <= M (친구 관계의 수) <= 50,000

def bfs(s):
    global visit

    que = [s]
    visit[s] = True
    count = 0
    result = 0
    while que:
        que_ = []

        for q in que:
            result += count
            for c in range(1,N+1):
                if adj[q][c] == 1 and not visit[c]:
                    visit[c] = True
                    que_.append(c)
        
        que = que_
        count += 1
    return result


N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(M)]

adj = [[0] * (N+1) for _ in range(N+1)]

for a, b in arr:
    adj[a][b] = 1
    adj[b][a] = 1

# for a in adj:
#     print(a)

answer = 999999999
answer_idx = -1
for start in range(1,N+1):
    visit = [False] * (N+1)
    visit[start] = True
    result = bfs(start)
    # print('start : ' + str(start) + '  result : ' + str(result))
    if answer > result:
        answer_idx = start
        answer = result

print(answer_idx)