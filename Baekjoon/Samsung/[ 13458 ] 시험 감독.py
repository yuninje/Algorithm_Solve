N = int(input())
arr = list(map(int, input().split()))
B, C = list(map(int, input().split()))

for a in range(0,N):
    arr[a] -= B

answer = N

for a in arr:
    if a >= 0:
        if a % C == 0:
            answer += a // C
        else:
            answer += a // C + 1

print(answer)