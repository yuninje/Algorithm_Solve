def solution(people, limit):
    answer = 0
    people = sorted(people)
    max_people = len(people)-1
    min_people = 0
    while(True):
        if min_people > max_people:
            break
        elif min_people == max_people:
            answer+= 1
            break
            
        if people[max_people] + people[min_people] > limit:
            max_people += -1
            answer += 1
        elif people[max_people] + people[min_people] <= limit:
            max_people += -1
            min_people += 1
            answer += 1
    
    return answer