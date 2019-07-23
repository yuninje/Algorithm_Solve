N = int(input())

arr = [[0,0]]
for n in range(0,N):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(0,N+1)]

for i in range(N,0,-1):
    print(i)
