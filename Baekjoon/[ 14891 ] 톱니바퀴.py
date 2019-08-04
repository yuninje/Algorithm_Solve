def turnC(l): # 1
    temp = arr[l][0]
    for i in range(0, len(arr[l])):
        arr[l][-i] = arr[l][-i -1]
    arr[l][1] = temp

def turnRC(l): # -1
    temp = arr[l][0]
    for i in range(1,len(arr[l])):
        arr[l][i-1] = arr[l][i]
    arr[l][-1] = temp

arr = []
for i in range(0,4):
    line = input()
    line_ = []
    for c in range(0,8):
        line_.append(int(line[c]))
    arr.append(line_)

C = int(input())
move = []
for c in range(0,C):
    move.append(list(map(int, input().split())))
    move[c][0] -= 1

for c in move:
    list_ = []
    for a in range(0,len(arr)):
        list_.append([arr[a][6],arr[a][2]])

    if c[1] == 1:
        turnC(c[0])
    else:
        turnRC(c[0])

    cl = c[0]-1
    clt = -c[1]
    while cl >= 0: # <<
        if list_[cl][1] != list_[cl+1][0]:
            if clt == 1:
                turnC(cl)
            else:
                turnRC(cl)

            clt = -clt
            cl -= 1
        else:
            break
        
    cr = c[0]+1
    crt = -c[1]
    while cr <= 3:  # >>
        if list_[cr-1][1] != list_[cr][0]:
            if crt == 1:
                turnC(cr)
            else:
                turnRC(cr)
            crt = -crt
            cr += 1
        else:
            break
    
answer = 0
mult = 1
for a in arr:
    answer += a[0]*mult
    mult *= 2
print(answer)