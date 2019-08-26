# https://www.acmicpc.net/problem/8980
# 2 <= N(마을 수) <= 2000
# 1 <= C(트럭 용량) <= 10000
# 1 <= M(박스 개수) <= 10000

N, C = list(map(int, input().split()))
M = int(input())
arr = []
for m in range(0,M):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key= lambda x: [x[1], -x[2], x[0]])

dp = [0] * (N+1)
total = 0
for a in arr:
    start = a[0] 
    end = a[1]
    box = a[2]
    fullFlag = False
    MIN = box
    for town in range(start, end+1):
        if dp[town] ==  C:
            fullFlag = True
            break
        MIN = min(MIN, C-dp[town])
    if not fullFlag:
        for town in range(start, end):
            dp[town] += MIN
        total += MIN
print(total)
    

