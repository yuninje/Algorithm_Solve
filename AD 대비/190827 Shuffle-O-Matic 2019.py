# Shuffle-O-Matic 2019
# 4 <= N (카드 개수) <= 12
import sys

def dfs(ar, count):
    global ANSWER
    if count == 6:
        return
    if ar == result_arr_2 or ar == result_arr_1:
        ANSWER = min(ANSWER , count)

    origin = ar[:]
    for x in range(1,N):
        if x > N//2:
            x = N - x
        xx = N//2 + x -1
        while x > 0:
            temp = origin[xx]
            origin[xx] = origin[xx-1]
            origin[xx-1] = temp
            xx -= 2
            x -= 1
        # print('count : ' + str(count) + '   ar : ' + str(ar))
        dfs(origin, count+1)
    
T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ANSWER = 6
    result_arr_1 =  sorted(arr)
    result_arr_2 = sorted(arr, reverse = True)
    print('original arr : ' + str(arr))
    dfs(arr, 0)

    if ANSWER == 6:
        ANSWER = -1
    print('answer : ' +str(ANSWER))
