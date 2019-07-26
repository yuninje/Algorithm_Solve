# https://www.acmicpc.net/problem/9095
def solution(num, arr, n):
    if n == 0:
        solution(num-1, arr.copy(), 1)
        solution(num-2, arr.copy(), 2)
        solution(num-3, arr.copy(), 3)
    else:
        if num > 0:
            arr.append(n)

            solution(num-1, arr.copy(), 1)
            solution(num-2, arr.copy(), 2)
            solution(num-3, arr.copy(), 3)
        elif num == 0:
            arr_list.append(arr.copy())

T = int(input())
for test in range(1,T+1):
    N = int(input())
    arr_list = []
    solution(N, [],0)

    print(len(arr_list))