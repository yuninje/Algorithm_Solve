# https://www.acmicpc.net/problem/2651
L = int(input()) # 정비를 받지 않고 갈 수 있는 최대 거리
N = int(input()) # 정비소의 개수
drr = list(map(int, input().split())) # 정비소 사이의 거리
hrr = list(map(int, input().split())) # 정비소별 정비 시간
dp = [0] * (N+1)
dp[-2] = hrr[-1]
idx_list = [[] for _ in range(N+1)]
idx_list[-2] = [N]
for d1 in range(N-2, -1, -1):
    d = drr[d1+1]
    dp[d1] = dp[d1+1]
    idx = d1+1
    for d2 in range(d1+2, N+1):
        if d + drr[d2] <= L:
            d += drr[d2]
            if dp[d1] > dp[d2]:
                dp[d1] = dp[d2]
                idx = d2
        else:
            break
    dp[d1] += hrr[d1]
    idx_list[d1] = [d1+1] + idx_list[idx]
    
d = drr[0]
MIN = dp[0]
result = 0
for i in range(1, N+1):
    d += drr[i]
    if d > L:
        break
    if MIN > dp[i]:
        MIN = dp[i]
        result = i
print(dp[result])
print(len(idx_list[result]))
print((' ').join(map(str, idx_list[result])))