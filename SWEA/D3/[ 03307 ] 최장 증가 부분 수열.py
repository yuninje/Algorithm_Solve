# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBOKg-a6l0DFAWr
T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N
    for n in range(N):
        MAX = 0
        for m in range(n):
            if arr[m] < arr[n]:
                MAX = max(dp[m], MAX)
        dp[n] =  MAX + 1

    print('#' + str(test) + ' ' + str(max(dp)))