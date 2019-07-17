def solution(x, n):
    answer = []
    now = 0
    count = 0
    while(count != n):
        now += x
        answer.append(now)
        count += 1
        print("count : %d,  x : %d" %(count, x))
    return answer