# https://www.acmicpc.net/problem/1700

N, K = map(int, input().split())
arr = list(map(int, input().split()))
now = []
answer = 0
for i in range(K):
    # print(arr[i])
    # print(now)
    # print('=====================')
    if arr[i] in now:
        # print('이미있음')
        continue

    if len(now) < N:
        now.append(arr[i])
    else: 
        if N == 1:
            del now[0]
            now.append(arr[i])
        else:
            visit = [1] * N
            for j in range(i+1, K):
                for k in range(N):
                    if arr[j] == now[k]:
                        visit[k] = 0
                if sum(visit) == 1:
                    for k in range(N):
                        if visit[k] == 1:
                            del now[k]
                            now.append(arr[i])
                            break
                    break
            else:
                for k in range(N):
                    if visit[k] == 1:
                        del now[k]
                        now.append(arr[i])
                        break
        
        answer += 1

print(answer)