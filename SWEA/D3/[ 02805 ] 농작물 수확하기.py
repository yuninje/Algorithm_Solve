# test = int(input())
# for t in range(1,test+1):
#     N = int(input())
#     arr = [[0] * N for _ in range(0,N)]
#     total = 0
#     for r in range(0,N):
#         line = input()
#         for c in range(0,N):
#             arr[r][c] = int(line[c])
#             if r >= -c + N//2 and r >= c - N//2 and r <= -c + (N//2) * 3 and r <= c + N//2:
#                 total += arr[r][c]


#     print("#"+str(t) + " " + str(total))
test = int(input())
for t in range(1,test+1):
    N = int(input())
    arr = [[0] * N for _ in range(0,N)]
    total = 0
    for r in range(0,N//2):
        line = input()
        for c in range(0,N//2):
            if r >= -c + N//2:
                total += int(line[c])

        for c in range(N//2,N):
            if r >= c - N//2:
                total += int(line[c])

    for r in range(N//2,N):
        line = input()
        for c in range(0,N//2):
            if r <= c + N//2:
                total += int(line[c])

        for c in range(N//2,N):
            if r <= -c + (N//2) * 3:
                total += int(line[c])

    print("#"+str(t) + " " + str(total))
    # for a in arr:
    #     print(a)