# https://programmers.co.kr/learn/courses/30/lessons/42899
def solution(K, travel):
    answer = 0
    R = len(travel)
    C = K
    dp = [[0] * (C+1) for _ in range(R+1)]
    
    bt,bm,wt,wm = travel[0]
    dp[1][bt] = bm
    dp[1][wt] = max(dp[1][wt], wm)
    
    for r in range(1,R):
        bt,bm,wt,wm = travel[r]
            
        for c in range(K+1): 
            if dp[r][c] == 0:
                continue
            if c + bt <= K:
                dp[r+1][c+bt] = max(dp[r+1][c+bt], dp[r][c] + bm)
                answer = max(answer, dp[r+1][c+bt])
            if c + wt <= K:
                dp[r+1][c+wt] = max(dp[r+1][c+wt], dp[r][c] + wm)
                answer = max(answer, dp[r+1][c+wt])
    
    return answer