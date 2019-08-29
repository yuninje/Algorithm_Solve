T = int(input())
for test in range(1,T+1):
    N, L = list(map(int, input().split()))
    lines = [list(map(int, input().split())) for _ in range(0,L)]
    visit = [-1] * (N+1)
    xrr = []
    answer = 0
    lines = sorted(lines, key=lambda x: x[2])
    for l in lines:
        a = l[0]
        b = l[1]
        v = l[2]
        visit_a = visit[a]
        visit_b = visit[b]
        if visit_a == -1 and visit_b == -1:         # 
            visit[a] = len(xrr)
            visit[b] = len(xrr)
            xrr.append([a,b])
        elif visit_a == visit_b:                      # 같은 배열
            continue
        elif (visit_a != -1) and (visit_b != -1): # 병합
            if visit_b > visit_a:
                for x in xrr[visit_b]:
                    visit[x] = visit_a
                xrr[visit_a] += xrr[visit_b]
                xrr[visit_b] = []
            else:
                for x in xrr[visit_a]:
                    visit[x] = visit_b
                xrr[visit_b] += xrr[visit_a]
                xrr[visit_a] = []
        elif (visit_a != -1) and visit_b == -1:     # xrr[visit_a]에 추가
            xrr[visit_a].append(b)
            visit[b] = visit_a
        elif  visit_a == -1  and (visit_b != -1):     # xrr[visit_b]에 추가
            xrr[visit_b].append(a)
            visit[a] = visit_b
        answer += v
        if len(xrr[0]) == N:
            break
    print('#' + str(test) + ' ' + str(answer))