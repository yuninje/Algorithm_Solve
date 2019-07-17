def solution(bool_list, total_k, total_t, now):
    global answer
    flag = False
    for i in range(now,N):
        if not bool_list[i] and total_k + food[i][1] <= L:
            bool_list[i] = True
            solution(bool_list.copy(), total_k+ food[i][1], total_t + food[i][0], i)
            bool_list[i] = False
            flag = True
    
    if not flag and total_t > answer:
        answer = total_t

T = int(input())
for test in range(1,T+1):
    N, L = map(int, input().split())
    food = []
    for _ in range(0,N):
        food.append(list(map(int, input().split())))

    answer = 0
    solution([False for _ in range(0,N)], 0,0, 0)
    print("#" + str(test) + " "+ str(answer))