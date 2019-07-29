# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
def solution(a):
    start_1 = len(a)
    for i in range(0, len(a)):
        if a[i] == str(1):
            start_1 = i
            now = a[start_1]
            break

    answer = 1
    for i in range(start_1+1, len(a)):
        if now != a[i]:
            now = a[i]
            answer += 1
    
    return answer


T = int(input())
for test in range(1,T+1):
    N = input()
    print("#" + str(test) + " " + str(solution(N)))