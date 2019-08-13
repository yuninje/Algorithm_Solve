# https://www.acmicpc.net/problem/1806

N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

q = []

result = 100001
start = 0
end = -1
SUM = 0
for a in arr:
    end += 1
    SUM += a
    while end - start +1 >= result:
        SUM -= arr[start]
        start += 1
        
    while SUM >= S:
        if end - start +1 < result:
            result = end - start +1
        SUM -= arr[start]
        start += 1
if result == 100001:
    print(0)
else:
    print(result)
