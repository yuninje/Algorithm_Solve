# https://www.acmicpc.net/problem/6359
T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = [True] * (N+1)
    for i in range(2, N+1):
        idx = i
        while idx <= N:
            arr[idx] = not arr[idx]
            idx += i
    print(sum(arr)-1)