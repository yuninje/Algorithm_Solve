# https://www.acmicpc.net/problem/17394
# 2 <= n <= 1,000,000
# 2 <= A <= B <= 100,000
# N / 2
# N / 3
# N + 1
# N - 1

def bfs():
    que = [N]
    count = 0
    while que:
        que_ = []
        for n in que:
            if n < A:
                answer = min(answer, A-n+count)
                continue
            if A <= n <= B and primary[n]:
                return count
            if n > 0:
                que_.append(n-1)
            que_.append(n+1)
            que_.append(n//2)
            que_.append(n//3)

        que = que_
        count += 1

T = int(input())
# set primary
MAX = 100000
primary = [True] * (MAX+1)
primary[0] = False
primary[1] = False
for i in range(2,MAX+1):
    if primary[i]:
        k = 2
        while i * k <= MAX:
            primary[i * k] = False
            k += 1
    
for test in range(1,T+1):
    N, A, B = list(map(int, input().split()))
    for i in range(A, B+1):
        if primary[i]:
            print(bfs())
            break
    else:
        print('-1')

