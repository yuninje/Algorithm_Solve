# https://www.acmicpc.net/problem/11403

# 1 <= N <= 100  N : 정점의 개수
# arr[i][j] == 1  > i 에서 j로 가는 간선 존재

def dfs(start, now):
    for i in range(0,N):
        if arr_answer[start][i] != 1 and arr[now][i] == 1:
            arr_answer[start][i] = 1
            dfs(start, i)



N = int(input())
arr = []
for n in range(0,N):
    arr.append(list(map(int, input().split())))

arr_answer = [[0 for _ in range(0,N)] for __ in range(0,N) ]

for r in range(0,N):
    dfs(r,r)

for line in arr_answer:
    for a in line:
        print(str(a),end=" ")
    print()