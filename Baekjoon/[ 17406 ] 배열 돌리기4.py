# https://www.acmicpc.net/problem/17406
# N * M 배열
# arr의 값 = min(sum(arr[0]), sum(arr[1]), ...)
# 회전연산 : (r,c,s)  
# 3 ≤ N, M ≤ 50
# 1 ≤ K ≤ 6
# 1 ≤ A[i][j] ≤ 100
# 1 ≤ s
# 1 ≤ r-s < r < r+s ≤ N
# 1 ≤ c-s < c < c+s ≤ M

def dfs(count):
    if count == K:
        cal()
        return

    for k in range(K):
        if visit[k]:
            continue
        visit[k] = True
        turn(k)
        dfs(count+1)
        reverse_turn(k)
        visit[k] = False

def turn(idx):
    kr = krr[idx]
    sr = kr[0] - kr[2] - 1
    er = kr[0] + kr[2] - 1
    sc = kr[1] - kr[2] - 1
    ec = kr[1] + kr[2] - 1
    while er-sr > 1 :

        temp_1 = arr[sr][ec]
        temp_2 = arr[er][ec]
        temp_3 = arr[er][sc]

        # 상 가로  좌 -> 우
        for c in range(ec, sc, -1):
            arr[sr][c] = arr[sr][c-1]
        # 우 세로  상 -> 하
        for r in range(er, sr, -1):
            arr[r][ec] = arr[r-1][ec]
        # 하 가로  우 -> 좌
        for c in range(sc, ec):
            arr[er][c] = arr[er][c+1]
        # 좌 세로  하 -> 상
        for r in range(sr, er):
            arr[r][sc] = arr[r+1][sc]
        arr[sr+1][ec] = temp_1
        arr[er][ec-1] = temp_2
        arr[er-1][sc] = temp_3
        
        sr += 1
        er -= 1
        sc += 1
        ec -= 1

def reverse_turn(idx):
    kr = krr[idx]
    sr = kr[0] - kr[2] - 1
    er = kr[0] + kr[2] - 1
    sc = kr[1] - kr[2] - 1
    ec = kr[1] + kr[2] - 1
    while er-sr > 1 :
        temp_1 = arr[sr][sc]

        # 상 가로  좌 -> 우
        for c in range(sc, ec):
            arr[sr][c] = arr[sr][c+1]
        # 우 세로  상 -> 하
        for r in range(sr, er):
            arr[r][ec] = arr[r+1][ec]
        # 하 가로  우 -> 좌
        for c in range(ec, sc, -1):
            arr[er][c] = arr[er][c-1]
        # 좌 세로  하 -> 상
        for r in range(er, sr,-1):
            arr[r][sc] = arr[r-1][sc]

        arr[sr+1][sc] = temp_1
        
        sr += 1
        er -= 1
        sc += 1
        ec -= 1
    return
def cal():
    global MIN
    for r in range(R):
        SUM = sum(arr[r])
        MIN = min(MIN, SUM)
R,C,K = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]
krr = [list(map(int, input().split())) for _ in range(K)]
MIN = 99999999999
visit = [False] * K
dfs(0)
print(MIN)