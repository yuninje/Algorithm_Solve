# https://www.acmicpc.net/problem/4195
import sys
I = sys.stdin.readline
T = int(I())
for test in range(1,T+1):
    N = int(I())
    arr = [list(I().split()) for _ in range(N)]

    visit = {}
    lists = []

    for a, b in arr:
        if a in visit and b in visit:
            if visit[a] == visit[b]:
                pass
            else:
                low = min(visit[a], visit[b])
                high = max(visit[a], visit[b])

                for name in lists[high]:
                    visit[name] = low
                    lists[low].append(name)
                lists[high] = []

        elif a in visit:
            visit[b] = visit[a]
            lists[visit[a]].append(b)
        elif b in visit:
            visit[a] = visit[b]
            lists[visit[b]].append(a)
        else:
            visit[a] = len(lists)
            visit[b] = len(lists)
            lists.append([a,b])
        print(len(lists[visit[a]]))