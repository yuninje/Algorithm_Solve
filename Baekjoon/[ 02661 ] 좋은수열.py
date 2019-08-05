# https://www.acmicpc.net/problem/2661

def dfs(str, count):
    global answer
    count += 1
    if len(answer) != 0:
        return
    if not check(str):
        return
    if count == N:
        answer.append(str)
        return
    dfs(str+"1", count)
    dfs(str+"2", count)
    dfs(str+"3", count)
    

def check(str):
    # 끝에거 기준으로만 체크
    for i in range(0,len(str) // 2):
        if str[-1-i:] == str[(-1-i)*2:-1-i]:
            return False
    return True

N = int(input())
answer = []
dfs("",-1)
print(answer[0])