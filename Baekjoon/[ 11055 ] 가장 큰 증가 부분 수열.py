# https://www.acmicpc.net/problem/11055
N = int(input())

arr = [0] + list(map(int, input().split()))

M = [0 for _ in range(0,len(arr))]
S = [0 for _ in range(0,len(arr))]

M[1] = arr[0]
S[1] = arr[0]

for i in range (1,N+1):
    for j in range(0, i):
        if M[j] < arr[i]:
            if S[i] == 0:
                S[i] = S[j] + arr[i]
            else:
                S[i] = max(S[i], S[j]+arr[i])
    M[i] = arr[i]
    print(str(i) + "  >> M[i] = " + str(M[i]) +  "    ,   S[i]  : " + str(S[i]))

print(max(S))