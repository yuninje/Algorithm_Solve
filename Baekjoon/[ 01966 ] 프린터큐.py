# https://www.acmicpc.net/problem/1966
import sys
I = sys.stdin.readline

T = int(I())
for test in range(1,T+1):
    N, M = list(map(int, I().split()))
    arr = list(map(int, I().split()))
    sarr = sorted(arr, reverse=True)
    
    now_ = 0
    for n in range(N):
        for now__ in range(now_, now_ + N):
            now = now__ % N
            if sarr[n] == arr[now]:
                arr[now] = -1
                now_ = now+1
                break
        if now_ - 1 == M:
            print(n+1)
            break