# https://www.acmicpc.net/problem/15663
# 1 <= M <= N <= 8
# 1 <= arr[n] <= 10,000
def permanent(count):
    if count == M:
        copy_nrr = [0] * M
        for m in range(M):
            if nrr[m] == -1:
                return
            copy_nrr[m] = nrr[m]
        answer.append(copy_nrr)
        return

    for i in range(N):
        if visit[i]:
            continue
        visit[i] = True
        nrr[count] = arr[i]
        permanent(count+1)
        nrr[count] = -1
        visit[i] = False

N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
visit = [False] * N
answer = []
nrr = [-1] * M
permanent(0)

before = [-1] * M
answer = sorted(answer, key= lambda x: [x[m] for m in range(M)])
for a in answer:
    for m in range(M):
        if before[m] != a[m]:
            print(' '.join(list(map(str, a))))
            break
    before = a