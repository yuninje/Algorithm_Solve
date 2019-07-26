# https://www.acmicpc.net/problem/3190
# 사과를 먹으면 뱀의 길이가 늘어난다.
# 뱀이 벽 또는 자신의 몸과 부딛히면 끝
# N * N  (2 <= N <= 100 
# )  , 보드의 상하좌우의 끝에 벽
#  게임 시작시 뱀은 맨위 맨좌측
#  뱀의 길이는 1,  처음 방향 : 오른쪽
# 몸길이를 늘려 머리를 다음칸에 위치
# 이동칸에 사과가 있다면 사과가 없어지고 꼬리 그대로 ( 길이 늘어남 )
# 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워줌 ( 길이 그대로 )

N = int(input())
arr = [['O' for _ in range(0,N+2)] for __ in range(0,N+2)]
K = int(input())
apples = []
for k in range(0,K):
    apples.append(list(map(int, input().split())))
for a in apples:
    arr[a[0]][a[1]] = 'A'   # 사과
arr[1][1] = 'S' # 뱀

for n in range(0,N+2):
    arr[0][n] = 'X'
    arr[N+1][n] = 'X'
    arr[n][0] = 'X'
    arr[n][N+1] = 'X'
    
L = int(input())    # 1 <= L <= 100
CX = [[0,0] for _ in range(0,L)] #  x <= 10000  L : 왼쪽 90도  D : 오른쪽 90도
for l in range(0,L):
    line = input().split()
    CX[l][0] = int(line[0]) 
    if line[1] == 'D':  
        CX[l][1] = 1
    else:
        CX[l][1] = -1
CX.append([10001,0])
dir = [[0,1],[1,0],[0,-1],[-1,0]]

dirIndex = 0
time = 0
orderCount = 0
size = 1


# 자기 몸 부딛힘
# 벽 부딛힘
boolList = [[False for _ in range(0,N+2)] for __ in range(0,N+2)]
for n in range(0,N+2):
    boolList[0][n] = True
    boolList[N+1][n] = True
    boolList[n][0] = True
    boolList[n][N+1] = True
boolList[1][1] = True

head = [1,1]
tail = [1,1]
print("=============================time : " + str(time))
for a in arr:
    print(a)

dirList = [[-1,-1, 0]]
while True:
    print("time : " + str(time))
    print("now head : " + str(head[0]) + ","+str(head[1]))
    print("now tail : " + str(tail[0]) + ","+str(tail[1]))
    head[0] += dir[dirIndex][0]
    head[1] += dir[dirIndex][1]
    if boolList[head[0]][head[1]]:
        # game end
        break

    boolList[head[0]][head[1]] = True
    if arr[head[0]][head[1]] == 'A':
        size +=1
        print(size)
        arr[head[0]][head[1]] = 'S'
    else:
        arr[head[0]][head[1]] = 'S'
        boolList[tail[0]][tail[1]] = False
        arr[tail[0]][tail[1]] = 'O'
        
        if len(dirList) >= 2:
            if dirList[1][0] == tail[0] and dirList[1][1] == tail[1]:
                dirList.remove(dirList[0])
        tail[0] += dir[dirList[0][2]][0]
        tail[1] += dir[dirList[0][2]][1]
    time += 1
    print("=============================time : " + str(time))
    for a in arr:
        print(a) 
    if time ==  CX[orderCount][0]:
        dirIndex += CX[orderCount][1]
        dirIndex %= 4
        dirList.append([head[0],head[1],dirIndex])
        orderCount += 1
        
print(time+1)


