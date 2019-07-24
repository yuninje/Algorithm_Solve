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
    arr[a[0]][a[1]] = 'A'
arr[1][1] = 'S' # 뱀

for n in range(0,N+2):
    arr[0][n] = 'X'
    arr[N+1][n] = 'X'
    arr[n][0] = 'X'
    arr[n][N+1] = 'X'
    
L = int(input())    # 1 <= L <= 100
X = [0 for _ in range(0,L)] #  x <= 10000   시간
C = [0 for _ in range(0,L)] #  L : 왼쪽 90도  D : 오른쪽 90도
for l in range(0,L):
    line = input().split()
    X[l] = int(line[0]) 
    if line[1] == 'D':  
        C[l] = 1
    else:
        C[l] = -1

dir = [[0,1],[1,0],[0,-1],[-1,0]]
snake = [1,1]
dirIndex = 0
time = 0
orderCount = 0
size = 1



for a in arr:
    print(a)


while True:
    # for s in range(0,size):
    #     arr[snake[0]+dir[0]][snake[1]+dir[1]] = 'S'
    #     arr[snake[0]][snake[1]] = 'O'
    
    time += 1
    if time ==  X[orderCount]:
        dirIndex += C[orderCount]
        dirIndex %= 4


