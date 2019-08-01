# https://www.acmicpc.net/problem/9012
import sys
I = sys.stdin.readline

T = int(I())
for test in range(1,T+1):
    line = I().strip()

    if len(line) %2 == 1:
        print("NO")
        continue
    stack = []
    for l in line:
        if l == '(':
            stack.append('(')
        else:
            if len(stack) > 0:
                del stack[-1]
            else:
                stack.append(1)
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")