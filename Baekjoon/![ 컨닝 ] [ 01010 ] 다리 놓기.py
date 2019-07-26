# https://www.acmicpc.net/problem/1010
T = int(input())

for test in range(0,T):
    N , M= list(map(int,input().split()))

    result = 1
    for i in range(M-N+1,M+1):
        result *= i
    
    for i in range(1,N+1):
        result /= i


    print(int(result))