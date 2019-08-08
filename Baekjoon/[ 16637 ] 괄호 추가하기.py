# https://www.acmicpc.net/problem/16637

def dfs(count, total):
    global answer
    if count >= N:
        if answer < total:
            answer = total
        return
    
    # if dp[count] < total:   이부분을 넣으면 시간 감소 가능한데
    #     dp[count] = total    실패뜸 ㅜㅜㅜ
    # else:
    #     return
    
    
    #            num      oper         num          oper            num         oper
    # 뒤가 괄호  total arr[count] ( arr[count+1] arr[count+2] arr[count+3] ) arr[count+4]
    if count+3 < N:
        dfs(count+4, eval(str(total) + arr[count] + str(eval(arr[count+1:count+4]))))
    
    # 뒤 괄호 x
    dfs(count+2, eval(str(total) + arr[count:count+2]))
    

N = int(input())
arr = input()
answer = -2**31
dp = [-2**31] * N
dfs(1,int(arr[0]))
print(answer)
print(dp)