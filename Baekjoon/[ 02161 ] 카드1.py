# https://www.acmicpc.net/problem/2161

N = int(input())
que = []
for n in range(N):
    que.append(n+1)
result = []
flag = True
while que:
    if flag:
        result.append(que.pop(0))
        flag = False
    else:
        que.append(que.pop(0))
        flag = True

print(' '.join(list(map(str,result)))) 