# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    N = len(priorities)
    val = priorities[location]
    
    pri_ = sorted(priorities, reverse =True)
    
    idx = 0
    sort_i = 0
    last = 0
    while True:
        if priorities[idx] == pri_[sort_i]:
            if pri_[sort_i] == val:
                break
            priorities[idx] = 0
            sort_i += 1
            last = idx
            answer += 1
        idx += 1
        idx %= N
        
    for n in range(N):
        if priorities[last] == val:
            answer += 1
        if last == location:
            break
        last += 1
        last %= N        
    
    return answer