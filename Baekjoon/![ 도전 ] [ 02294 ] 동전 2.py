# https://www.acmicpc.net/problem/2294
N, K = list(map(int, input().split()))
arr = []
for n in range(0,N):
    arr.append(int(input()))
arr = sorted(arr)
dp = [0 for _ in range(0,K+1)]
for i in range(1,K+1):
    for a in range(0,N):
        if i - arr[a] >= 0:
            if dp[i-arr[a]] != -1:
                if dp[i] == 0:
                    dp[i] = dp[i-arr[a]] +1
                else:
                    dp[i] = min(dp[i], dp[i-arr[a]]+1)
        else:
            break

    if dp[i] == 0:
        dp[i] = -1


    
# print(dp[K])


for d in dp:
    print(d)
    
    
        
        
