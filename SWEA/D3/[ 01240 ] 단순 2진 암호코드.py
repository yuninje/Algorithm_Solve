# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD
# 1 <= N < 50 , 1 <= M < 100
#  

def cal(word):
    num1 = 0
    num2 = 0
    for w in range(0,len(word)):
        if w % 2 == 0 or w == len(word)-1:
            num2 += int(word[w])
        else:
            num1 += int(word[w])
    total = num1 * 3 + num2
    print('total : ' + str(total))
    if total % 10 == 0:
        return True
    else:
        return False

import sys
I = sys.stdin.readline
T = int(I())
for test in (1,T+1):
    R, C = list(map(int, I().split()))
    arr = []
    num = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    for r in range(0,R):
        arr.append(I())

    result = ''
    word = ''
    count = 0
    for a in arr:
        flag = 0
        for idx in range(0,len(a), 1):
            if flag != 0:
                flag -= 1
            else:
                if idx > len(a)-7:
                    break
                for n in range(0,len(num)):
                    if a[idx:idx+7] == num[n]:
                        result += str(n)
                        flag = 6
                        break
        count += 1
        if result != '' and word == '':
            for r in result:
                word += r

    total = 0

    if cal(word):
        for w in word:
            total += int(w)
        print("#"+str(test) + " " + str(total))
    else:
        print("#"+str(test) + " 0")


