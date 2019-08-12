def chi_home():
    global dis
    for c in chi:
        distance = 0
        for h in home:
            distance += abs(c[0]-h[0]) + abs(c[1]-h[1])
        dis.append(distance)
N, M = list(map(int, input().split()))
arr = []
chi = []
home = []
dis = []
for r in range(0,N):
    arr.append(list(map(int,input().split())))
    for c in range(0,N):
        if arr[r][c] == 1:
            home.append([r,c])
        elif arr[r][c] == 2:
            chi.append([r,c])

chi_home()
sorted(dis, reverse = True)
print(dis)

