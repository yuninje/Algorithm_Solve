A, B, V = list(map(int, input().split()))

N = (V-A) // (A-B)
if (A-B) * N + A == V:
    print(N+1)
else:
    print(N+2)