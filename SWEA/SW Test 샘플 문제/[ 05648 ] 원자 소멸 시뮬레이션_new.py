T = int(input())
dir = [[0,1], [0,-1], [-1,0], [1,0]]
# x, y, d, K
for t in range(1,T+1):
    N = int(input())
    size = 1000
    total_size = size * 4 + 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    for a in range(len(arr)):
        arr[a][0] = arr[a][0] * 2 + size*2
        arr[a][1] = arr[a][1] * 2 + size*2
    # -size ~ size
    Map = [[-1] * total_size for _ in range(total_size)] # 기본 -1

    time = 0
    answer = 0
    while time < total_size:
        time += 1
        removeList = []
        for i in range(len(arr)):
            
            arr[i][0] += dir[arr[i][2]][0]
            arr[i][1] += dir[arr[i][2]][1]
            x = arr[i][0]
            y = arr[i][1]
            if total_size <= x or x < 0 or total_size <= y or y < 0:
                removeList.append(i)
                continue 
            if Map[x][y] == -1: # 이동
                Map[x][y] = i
            else: # 폭발

                if Map[x][y] == -2: # 이미 폭발
                    pass
                else:                               # 지금 폭발
                    exist = Map[x][y]
                    answer += arr[exist][3]
                    removeList.append(exist)
                    Map[x][y] = -2
                
                removeList.append(i)
                answer += arr[i][3]
        
        for x,y,d,k in arr:
            if 0 <= x and x < total_size and 0 <= y and y <total_size:
                Map[x][y] = -1

        removeList = sorted(removeList, reverse = True)
        for r in removeList:
            del arr[r]

    print('#' + str(t) + ' ' + str(answer))