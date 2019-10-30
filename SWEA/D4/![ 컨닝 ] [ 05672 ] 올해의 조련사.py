T = int(input())
for test in range(1,T+1):
    N = int(input())
    orr = [input().strip() for _ in range(N)]   
    arr = list(map(lambda x : ord(x), orr))
    rrr = []
    for a in range(N-1, -1, -1):
        rrr.append(ord(orr[a]))
    print(arr)
    answer = []
    ai = 0
    ri = 0

    while ai + ri < N:
        if arr[ai] > rrr[ri]:
            answer.append(chr(rrr[ri]))
            ri += 1
        elif arr[ai] < rrr[ri]:
            answer.append(chr(arr[ai]))
            ai += 1
        else:
            now = arr[ai]
            i = 1
            while ai + ri + 2 * i < N:
                if arr[ai+i] < now:
                    if arr[ri+i] <= arr[ai+i]:
                        for j in range(ri, ri+i+1):
                            answer.append(chr(arr[j]))
                        ri += i+1
                    else:
                        for j in range(ai, ai+i+1):
                            answer.append(chr(arr[j]))
                        ai += i+1
                elif arr[ai+i] == now:
                    if arr[ri+i] < arr[ai+i]:
                        for j in range(ri, ri+i+1):
                            answer.append(chr(arr[j]))
                        ri += i+1
                    elif arr[ri+i] == arr[ai+i]:
                        i += 1
                    else:
                        for j in range(ai, ai+i+1):
                            answer.append(chr(arr[j]))
                        ai += i+1 
                else:   # arr[ai+1] > now
                    if arr[ri+i] <= now:
                        for j in range(ri, ri+i+1):
                            answer.append(chr(arr[j]))
                        ri += i+1
                    else:
                        for j in range(2 * i):
                            answer.append(chr(now)) 
                        ri += i
                        ai += i
        
    
    

    print('#' + str(test) + ' ' + ''.join(answer))