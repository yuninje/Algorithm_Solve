# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
# N % 4 == 0
#  8 <= N <= 28
# 

def find_num():
    for a in range(0,4):
        m = a * (N//4)
        n = ''
        for i in range(m,m+(N//4)):
            n += arr[i]
        num.append(n)

def turn():
    temp = arr[-1]
    for a in range(N-1, 0, -1):
        arr[a] = arr[a-1]
    arr[0] = temp

T = int(input())
for test in range(1,T+1):    
    N, K = list(map(int, input().split()))
    arr = list(input())
    answer = 0

    num = []
    find_num()
    # now
    for i in range((N//4)-1):
        #1 ~ K
        turn()
        find_num()
    num = list(map(lambda x : int(x,16), num))

    num = sorted(num, reverse=True)
    # print(num)
    before = num[0]
    idx = 2
    if K==1:
        answer = num[0]
    else:
        for n in range(1,len(num)):
            if before == num[n]:
                continue
            if idx == K:
                answer = num[n]
                break
            before = num[n]
            idx += 1

    print('#'+str(test) + ' ' + str(answer))
