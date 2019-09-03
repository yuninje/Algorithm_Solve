# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
def solution(prices):
    answer = [0] * len(prices)
    
    before = 0
    value = 0
    queue = [[0,len(prices)-1]]
    for p in range(len(prices)-2,-1,-1):
        q = 0
        while queue:
            if prices[p] <= queue[q][0]:
                del queue[q]
            else:# pr[p] > qu[q]
                answer[p] = queue[0][1]-p
                queue.insert(0,[prices[p],p])
                break
            
    return answer