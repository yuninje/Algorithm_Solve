N = int(input())
d = []
d.append(0)
d.append(1)
d.append(1)
d.append(2)

for i in range(4,91):
  d.append(d[i-1] + d[i-2])

print(d[N])