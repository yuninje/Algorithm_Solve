# https://www.acmicpc.net/problem/6603
# k > 6

def find(count, before):
    count += 1
    if count == length:
        make(-1,-1)
        return
    
    for i in range(before+1, length):
        result[count] = arr[i]
        find(count, i)
    
def make(count, before):
    count += 1
    if count == 6:
        for p in print_arr:
            print(p, end=' ')
        print()
        return
    
    for i in range(before+1, K):
        print_arr[count] = result[i]
        make(count, i)
    


while True:
    line = list(map(int,input().split()))
    if len(line) == 1:
        break
    K = line[0]
    arr = line[1:]
    length = len(arr)
    result = [0] * K
    print_arr = [0] * 6
    find(-1, -1)
    print()