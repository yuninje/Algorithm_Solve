# https://www.acmicpc.net/problem/6549

line = input().split()
N = int(line[0])
while N != 0:
    arr = list(map(int, line[1:]))

    stack = [[arr[0],0]]
    MAX = 0
    for i in range (1,len(arr)):
        # print(str(i) + " -  stack : " + str(stack))
        if arr[i] < arr[i-1]:
            while len(stack) != 0:
                if stack[-1][0] > arr[i]:
                    top = stack.pop()
                    # print("top : " + str(top))
                    MAX = max(MAX, top[0] * ( i - top[1] ))
                    
                else:
                    break
            stack.append([arr[i], top[1]])
        else: # arr[i] > arr[i-1]
            stack.append([arr[i], i])
            
    for s in stack:
        MAX = max(s[0] * (len(arr)-s[1]), MAX)

    print(MAX)

    # next test case
    line = input().split()
    N = int(line[0])
    

