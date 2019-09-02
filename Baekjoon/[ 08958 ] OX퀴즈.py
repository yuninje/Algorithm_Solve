# https://www.acmicpc.net/problem/8958

T = int(input())
arr = [input() for _ in range(T)] 
for a in arr:
    flag = False
    answer = 0
    for i in range(len(a)):
        if a[i] == 'O':
            if not flag:
                flag = True
                plus = 1
            else:
                plus += 1
            answer += plus
        else:
            flag = False
    print(answer)