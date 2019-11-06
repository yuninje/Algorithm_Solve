
T = int(input())
for test in range(1,T+1):
    L = int(input())
    answer = 0
    
    for l in range(L, 2, -2):
        answer += L - l + 1

    print('#' + str(test) + ' ' + str(answer))