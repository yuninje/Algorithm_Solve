# https://www.acmicpc.net/problem/2529
# 2 <= N <= 9
def dfs(now, count, total):
    global MIN, MAX
    if count == N:
        if int(MIN) > int(total):
            MIN = total
        if int(MAX) < int(total):
            MAX = total
        return
    for i in range(0,10):
        if visit[i]:
            continue
        if s[count] == '<' and now >= i:
            continue
        elif s[count] =='>' and now <= i:
            continue
        visit[i] = True
        dfs(i, count+1, total + str(i))
        visit[i] = False


N = int(input())
s = input().split()
visit = [False]*10
MIN = '9999999999'
MAX = '0'
for i in range(0,10):
    visit[i] = True
    dfs(i, 0, str(i))
    visit[i] = False
print(MAX)
print(MIN)
