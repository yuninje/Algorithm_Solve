def dfs(now, count):
    global MIN
    if N//2 == count:
        dif = cal()
        MIN = min(MIN, dif)
        return

    for n in range(now+1,N):
        visit[n] = True
        dfs(n, count+1)
        visit[n] = False

def cal():
    total = 0
    t1 = []
    t2 = []
    for n in range(0,N):
        if visit[n]:
            t1.append(n)
        else:
            t2.append(n)
    for i in range(0,N//2):
        for j in range(i+1,N//2):
            total += arr[t1[i]][t1[j]]
            total += arr[t1[j]][t1[i]]
            total -= arr[t2[i]][t2[j]]
            total -= arr[t2[j]][t2[i]]
    return abs(total)

N = int(input())
arr = []
MIN = 9223372036854775807 # python 에서 가질수 있는 최대값
for r in range(0,N):
    arr.append(list(map(int, input().split())))
visit = [False] * N
dfs(-1, 0)
print(MIN)