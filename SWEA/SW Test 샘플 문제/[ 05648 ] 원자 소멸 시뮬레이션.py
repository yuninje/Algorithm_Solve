# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
#
T = int(input())
dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]
#      상(0), 하(1), 좌(2), 우(3)
FIELD = 1000
MAX_FIELD = 4 * FIELD
arr = [[-1] * (MAX_FIELD + 1) for _ in range(0, MAX_FIELD + 1)]
for test in range(1, T + 1):
    N = int(input())
    point = []
    for p in range(0, N):
        point.append(list(map(int, input().split())))
        point[p][0] += MAX_FIELD//2 + point[p][0]
        point[p][1] += MAX_FIELD//2 + point[p][1]

    result = 0
    for i in range(0, MAX_FIELD):
        bump = []
        for p in range(0, len(point)):
            point[p][0] += dir[point[p][2]][0]
            point[p][1] += dir[point[p][2]][1]
            x = point[p][0]
            y = point[p][1]
            if MAX_FIELD >= x and x >= 0 and MAX_FIELD >= y and y >= 0:
                if arr[x][y] == -1:  # point 없음
                    arr[x][y] = p
                elif arr[x][y] == -2:  # bump
                    result += point[p][3]
                    bump.append(p)
                else:
                    result += point[p][3]
                    result += point[arr[x][y]][3]
                    bump.append(p)
                    bump.append(arr[x][y])
                    arr[x][y] = -2
        for p in point:
            x = p[0]
            y = p[1]
            if MAX_FIELD >= x and x >= 0 and MAX_FIELD >= y and y >= 0:
                arr[x][y] = -1
        bump = sorted(bump, reverse=True)
        for b in bump:
            del point[b]
    print('#' + str(test) + ' ' + str(result))