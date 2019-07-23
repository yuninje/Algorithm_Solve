N, K = list(map(int, input().split()))
arr = []
for n in range(0,N):
    arr.append(int(input()))

dp = [0 for _ in range(0,K+1)]
for i in range(1,K+1):

    for a in range(0,N):
        if(dp[i-arr[a]] != -1):
            dp[i] = min(dp[i-arr[a]]+1, dp[i])
    


print(dp[K])
    
    
        
        
