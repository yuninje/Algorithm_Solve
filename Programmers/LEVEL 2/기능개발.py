def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(0,len(progresses)):
        if (100 - progresses[i] ) % speeds[i] != 0:
            day.append((100 - progresses[i]) // speeds[i] +1)
        else:
            day.append((100-progresses[i])// speeds[i])
    count = 1
    stop = 0
    print(day)
    
    for i in range(1, len(day)):
        
        if day[stop] >= day[i]:
            count += 1
        elif day[stop] <day[i]:
            answer.append(count)
            stop = i
            count = 1
        if i == len(day)-1:
            answer.append(count)
    return answer