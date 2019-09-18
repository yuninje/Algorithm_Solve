#https://programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    answer = 0
    N = len(money)
    money.insert(0,0)
    
    dp_first = [0] * (N+1) # first 사용
    dp_first[1] = money[1]
    dp_first[2] = money[1]
    dp_last = [0] * (N+1)  # last 사용
    dp_last[1] = 0
    dp_last[2] = money[2]
    for n in range(3,N+1):
        dp_first[n] = max(dp_first[n-1], dp_first[n-2] + money[n])
        dp_last[n] = max(dp_last[n-1], dp_last[n-2] + money[n])
    return max(dp_first[N-1], dp_last[N])