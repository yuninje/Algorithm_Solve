import math

T = int(input())
for test in range(1,T+1):
    n2 = input()
    n3 = input()

    num2 = 0
    num3 = 0
    # print('n2 = ' + str(n2))
    # print('n3 = ' + str(n3))
    for n in range(len(n2)):
        if n2[n] == '1':
            num2 += 2 ** int(len(n2)-n-1)

    for n in range(len(n3)):
        if n3[n] != '0':
            num3 += 3 ** int(len(n3)-n-1) * int(n3[n])
    # print('num2 = ' + str(num2))
    # print('num3 = ' + str(num3))

    arr = set()

    for n in range(len(n2)):
        if n2[n] == '0':
            num2_ = num2 + 2**(len(n2)-n-1)
        else:
            num2_ = num2 - 2 ** (len(n2)-n-1)
        
        arr.add(num2_)
    answer = 0
    for n in range(len(n3)):
        if n3[n] == '0':
            num3_ = num3 + 3**(len(n3)-n-1)
            if num3_ in arr:
                answer = num3_
                break
            num3_ = num3 + (3 ** (len(n3)-n-1)) * 2
            if num3_ in arr:
                answer = num3_
                break
        if n3[n] == '1':
            num3_ = num3 - 3** (len(n3)-n-1)
            if num3_ in arr:
                answer = num3_
                break
            num3_ = num3 + 3 ** (len(n3)-n-1)
            if num3_ in arr:
                answer = num3_
                break
        if n3[n] == '2':
            num3_ = num3 - 3** (len(n3)-n-1)
            if num3_ in arr:
                answer = num3_
                break
            num3_ = num3 - (3 ** (len(n3)-n-1)) * 2
            if num3_ in arr:
                answer = num3_
                break

    print('#' + str(test) + ' ' + str(answer))