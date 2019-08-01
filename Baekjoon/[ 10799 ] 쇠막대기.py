# https://www.acmicpc.net/problem/10799
import sys
I = sys.stdin.readline

line = I()
stack = 0
answer = 0
for l in line:
    if l == '(':
        stack += 1
        flag = True
    elif l == ')' and flag:
        stack -= 1
        answer += stack
        flag = False
    elif l == ')':
        answer += 1
        stack -= 1
print(answer)