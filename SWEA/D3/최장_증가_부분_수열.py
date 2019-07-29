# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBOKg-a6l0DFAWr
def solution(now):
    global list_
    global arr
    answer = []
    answer.append(int(0))
    if list_[now] == -1:
        for i in range(now+1, len(arr)):
            if arr[now] < arr[i] :
                if list_[i] == -1:
                    list_[i] = solution(i)
                answer.append(list_[i])
        #print("answer : " + str(answer))
        list_[now] = max(answer)+1

    return list_[now]



T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    list_ = [-1 for _ in range(0,N)]
    for i in range(0,N):
        solution(i)
    
    print("#"+str(test) + " " + str(max(list_)))