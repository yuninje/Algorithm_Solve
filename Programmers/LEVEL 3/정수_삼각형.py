def solution(triangle):
    answer = []
    
    answer.append([0])
    answer.append([0,0])
    for n in range(2,len(triangle)+2):
        line = []
        line.append(0)
        for i in range(1,n):
            line.append(max(answer[n-1][i-1], answer[n-1][i]) + triangle[n-2][i-1])
        line.append(0)
        answer.append(line)
    
    return max(answer[len(triangle)+1])