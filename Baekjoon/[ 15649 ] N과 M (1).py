# https://www.acmicpc.net/problem/15649
def fun(count):
    if count == M:
        print(' '.join(list(map(str, arr))))
        return
    for n in range(1,N+1):
        if visit[n]:
            continue
        visit[n] = True
        arr[count] = n
        fun(count+1)
        visit[n] = False

N, M = list(map(int, input().split()))
arr = [0] * M
visit = [False] * (N+1)
fun(0)