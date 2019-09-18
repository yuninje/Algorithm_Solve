# https://programmers.co.kr/learn/courses/30/lessons/42899
def solution(K, travel):
    # 도보 시간, 도보 모금액, 자전거 시간, 자전거 모금액
    len_t = len(travel)
    dp = [[0] * (K+1) for _ in range(len_t+1)]
    dp[1][travel[0][0]] = travel[0][1]
    dp[1][travel[0][2]] = travel[0][3]
    for r in range(1,len_t): # 거리
        for c in range(K+1): # 시간
            # 도보
            if dp[r][c] == 0 :
                continue
            if c + travel[r][0] <= K:
                dp[r+1][c + travel[r][0]] = max(dp[r+1][c + travel[r][0]], dp[r][c] + travel[r][1])
            # 자전거
            if c + travel[r][2] <= K:
                dp[r+1][c + travel[r][2]] = max(dp[r+1][c + travel[r][2]], dp[r][c] + travel[r][3])
    return max(dp[len_t])