
T = int(input())
for test in range(1,T+1):
    r1, r2 = list(map(int, input().split()))
    arr1 = [input().strip() for _ in range(r1)]
    arr2 = [input().strip() for _ in range(r2)]

    sc = 0
    mc = 0
    bc = 0
    dot = 0
    record = []
    for ar in arr1:
        dot = 0    
        flag = True
        for a in ar:
            if a =='.' and flag:
                dot += 1
            else:
                if flag:
                    flag = False
                    record.append([sc,mc,bc,dot])
                if a == '(':
                    sc += 1
                elif a == ')':
                    sc -= 1
                elif a == '{':
                    mc += 1
                elif a == '}':
                    mc -= 1
                elif a == '[':
                    bc += 1
                elif a == ']':
                    bc -= 1
    
    smb = []
    for sv in range(1,21):
        for mv in range(1,21):
            for bv in range(1,21):
                for sc,mc,bc,dot in record:
                    if sv * sc + mv * mc + bc * bv == dot:
                        pass
                    else:
                        break
                else:
                    smb.append([sv,mv,bv])
                    
    # print('SV : ' + str(sv) + '  MV : ' + str(mv) + '  BV : ' + str(bv))
    sc = 0
    mc = 0
    bc = 0 
    answer = []
    for r in range(r2):
        before = -2
        for sv,mv,bv in smb:
            dot = sv * sc + mv * mc + bv * bc
            if before != -2:
                if dot != before:
                    answer.append(-1)
                    break
            before = dot
        else:
            answer.append(dot)
            
        for a in arr2[r]:
            if a == '(':
                sc += 1
            elif a == ')':
                sc -= 1
            elif a == '{':
                mc += 1
            elif a == '}':
                mc -= 1
            elif a == '[':
                bc += 1
            elif a == ']':
                bc -= 1
    print('#'+str(test) + ' ' + ' '.join(list(map(str, answer))))