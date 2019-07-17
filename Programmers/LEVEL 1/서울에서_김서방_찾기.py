def solution(seoul):
    return "김서방은 "+ str(list(filter(lambda i: seoul[i] == "Kim", range(0,len(seoul))))[0])+"에 있다"