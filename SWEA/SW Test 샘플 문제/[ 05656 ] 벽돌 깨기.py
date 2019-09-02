# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo

def dfs(count, total):
    if count == N:
        MAX = max(MAX, total)
        return
    for c in range(C):
        cr = crush(c)
        dfs(count+1, total + cr)
def crush(c):
    

    return count


T = int(input())
for test in range(1,T+1):
    N, C, R = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(H)]
    for a in arr:
        print(a)
    dfs(0,0)