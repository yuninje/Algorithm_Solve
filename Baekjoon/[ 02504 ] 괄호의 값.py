# https://www.acmicpc.net/problem/2504
# 1 <= len(str) <= 30
# ( ) = 2
# [ ] = 3
# ( X ) = 2 * X
# [ X ] = 3 * X
#  X Y = X + Y 
def check():
    stack = []
    for s in range(0,len(string)):
        stack.append(string[s])
    while True:
        for s in range(0,len(stack)-1):
            if stack[s] == '(' and stack[s+1] == ')':
                del stack[s+1]
                del stack[s]
                break
            elif stack[s] == '[' and stack[s+1] == ']':
                del stack[s+1]
                del stack[s]
                break
        else:
            if len(stack) == 0:
                return True
            else:
                return False
        


string = input()

if check():
    stack = []
    for s in range(0,len(string)):
        # (, [ 입력시 STACK 에 저장
        if string[s] == '(' or string[s] == '[':
            stack.append(string[s])
        # ), ] 입력시 (, [ 이 앞에 있는ㄴ지 확인
        elif string[s] == ')':
            if stack[-1] == '(':
                stack.pop() # ( pop
                stack.append('2')
            elif stack[-1].isdigit(): # 숫자
                top = stack.pop()
                top_ = stack.pop() # '('
                stack.append(str(int(top) * 2))
        elif string[s] == ']':
            if stack[-1] == '[':
                stack.pop() # ] pop
                stack.append('3')
            elif stack[-1].isdigit(): # 숫자
                top = stack.pop()
                top_ = stack.pop() # '['
                stack.append(str(int(top) * 3))
        
        while len(stack) >1 and stack[-1].isdigit() and stack[-2].isdigit():
            top1 = int(stack.pop())
            top2 = int(stack.pop())
            stack.append(str(top1 + top2))
    print(stack[0])
else:
    print(0)