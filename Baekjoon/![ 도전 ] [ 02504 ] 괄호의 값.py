# 1 <= len(str) <= 30
# ( ) = 2
# [ ] = 3
# ( X ) = 2 * X
# [ X ] = 3 * X
#  X Y = X + Y 

str = input()

answer = -1
stack = []
word = [['(',2], ['[', 3]]
for s in range(0,len(str)):
    if str[s] == '(' or str[s] == '[':
        stack.append(str[s])
    elif str[s] == ')':
        if stack[-1] == '(':
            stack.pop()
            stack.append(2)
        elif stack[-1].
