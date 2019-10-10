
#        N 개의 블록 ( 1 ~ N )
#        1 <= K <= N <= 200,000
#        1 <= W[i] <= 200,000   값이 클수록 남은 수명이 짧다.

#        초기 데이터 : K개 덩어리

#        i번째 덩어리는 S[i] 개의 연속된 블록에 저장
#         작은 번호의 블록부터 저장되어야함.
#         하나의 덩어리가 저장된 블록에는 다른 덩어리를 저장할 수 없다.

from queue import PriorityQueue

T = int(input())
for test in range(1,T+1):
    N, K = list(map(int, input().split()))
    W = list(map(int, input().split()))
    S = list(map(int, input().split()))
    answer = 0

    group = {} # HashMap
    # key : value, value list : idx
    for idx in range(N):
        if W[idx] in group:
            group[W[idx]] += [idx]
        else:
            group[W[idx]] = [idx]

    # dictionary > list 
    group = sorted(group.items())
    
    start = 0
    end = len(group)-1
    while start <= end:
        mid = (start + end) // 2

        # mid 로 계산.
        # 가능 >> start = mid+1
        # 불가능 >> end = mid-1



    answer = group[start-1][0]
    print('#' + str(test) + ' ' + str(answer))

