# https://www.acmicpc.net/problem/4949

line = input()
while len(line) != 1:
    noFlag = False
    stack = []
    for l in line:
        if l == '(' or l == '[':
            stack.append(l)
        elif l == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    noFlag = True
                    break
            else:
                noFlag = True
                break
        elif l == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    noFlag = True
                    break
            else:
                noFlag = True
                break
    if stack:
        noFlag = True
        
    if noFlag:
        print('no')
    else:
        print('yes')
    line = input()