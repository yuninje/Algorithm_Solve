# https://www.acmicpc.net/problem/6987

def dfs(me, you):
    global answer
    
    if me == 5:
        for i in range(len(crr)):
            breakFlag = False
            for r in range(6):
                for c in range(3):
                    if crr[i][r][c] != arr[r][c]:
                        breakFlag = True
                if breakFlag:
                    break
            if not breakFlag:
                answer[i] = 1
        return

    if you == 6:
        dfs(me+1,me+2)
        return

    # 승
    arr[me][0] += 1
    arr[you][2] += 1
    dfs(me,you+1)
    arr[me][0] -= 1
    arr[you][2] -= 1

    # 무
    arr[me][1] += 1
    arr[you][1] += 1
    dfs(me,you+1)
    arr[me][1] -= 1
    arr[you][1] -= 1

    # 패
    arr[me][2] += 1
    arr[you][0] += 1
    dfs(me,you+1)
    arr[me][2] -= 1
    arr[you][0] -= 1

    
        
brr = [list(map(int, input().split())) for _ in range(4)]

crr = []
for br in brr:
    line = []
    idx = 0
    l = []
    for b in br:
        l.append(b)
        idx += 1
        if (idx % 3 == 0):
            line.append(l)
            l = []
    crr.append(line)

arr = [[0] * 3 for _ in range(6)]
answer = [0] * len(crr)
dfs(0,1)
print(' '.join(list(map(str, answer))))