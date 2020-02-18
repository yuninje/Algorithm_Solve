dp = []
arr = []
def solution(ms):
    global dp
    global arr
    
    arr = [0] * ( len(ms) + 1 )
    arr[0] = ms[0][0]
    arr[1] = ms[0][1]
    for m in range(1, len(ms)):
        arr[m+1] = ms[m][1]

    la = len(arr)
    dp = [[-1] * la for _ in range(la)]
    answer = dfs(0,la-1)
    return answer

def dfs(s,e):
    global dp
    global arr
    if s == e - 1:
        return 0
    if dp[s][e] == -1:
        MIN = 999999999
        for m in range(s+1, e):
            MIN = min(dfs(s,m) + dfs(m,e) + arr[s] * arr[m] * arr[e], MIN)
        dp[s][e] = MIN
    return dp[s][e]