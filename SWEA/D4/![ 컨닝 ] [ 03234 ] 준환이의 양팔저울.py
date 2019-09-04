# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw&

def dfs(count, total_l, total_r):
    global answer
    global visit
    if count == N: 
        return 1
    for i in range(N):
        if visit[i]:
            continue
        visit[i] = True
        dfs(count+1, total_l+arr[i], total_r)
        if total_l >= total_r + arr[i]:
            dfs(count+1, total_l, total_r+arr[i])
        visit[i] = False

T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visit = [False] * N
    answer = dfs(0,0,0)
    
    print('#'+str(test) + ' ' + str(answer))
