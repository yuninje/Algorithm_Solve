arr = [[0] * 10 for _ in range(0,10)]
for r in range(0,10):
    line = input().split()
    for c in range(0,10):
        arr[r][c] = int(line[c])

