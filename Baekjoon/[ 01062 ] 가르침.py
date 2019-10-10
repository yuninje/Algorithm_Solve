# https://www.acmicpc.net/problem/1062
# 1 <= N <= 50
# 0 <= K <= 26
# 알파벳 소문자
# anta ~ tica >> a, n, t, i, c  ==> 5개는 필수
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def dfs(before, cnt):
    global answer
    if cnt == K:
        count = 0
        for i in range(N):
            for j in range(26):
                if brr[i][j]:
                    if alpha[j]:
                        pass
                    else:
                        break
            else:
                count += 1
        answer = max(answer, count)
        return
        
    if K - cnt > 25 - before:
        return

    for i in range(before+1, 26):
        if alpha[i] :
            continue
        alpha[i] = True
        dfs(i, cnt+1)
        alpha[i] = False

N, K = list(map(int, I().split()))
arr = [I().strip() for _ in range(N)]
if K < 5:
    print(0)
else:
    brr = [[False] * 26 for _ in range(N)]
    for n in range(N):
        for a in arr[n]:
            brr[n][ord(a)-ord('a')] = True
                    
    
    alpha = [False] * 26
    # a b c d e / f g h i j / k l m n o / p q r s t / u v w x y / z
    alpha[0] = True # a
    alpha[2] = True # c
    alpha[8] = True # i
    alpha[13] = True # n
    alpha[19] = True # t
    
    K -= 5
    answer = 0
    dfs(-1, 0)
    print(answer)