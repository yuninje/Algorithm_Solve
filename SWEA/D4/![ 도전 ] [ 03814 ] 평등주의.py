# T <= 20
# 2 <= N <= 10 ** 5
# 1 <= K <= 10 ** 9
# 1 <= arr[i] <= 10 ** 9


T = int(input())
for test in range(1,T+1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    answer = 0
    gap = [0] * (N-1)
    for i in range(N-1):
        gap[i] = arr[i+1]-arr[i]

    # arr[i] -= 1 >> gap[i-1] -= 1, gap[i] += 1
    

    print('#' + str(test) + ' ' + answer)