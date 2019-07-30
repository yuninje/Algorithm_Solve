# https://www.acmicpc.net/problem/2270
# A + B + C = N   ,     0 <= A, B, C <= n
# now : 1 >> a    , 2 >> b ,  3 >> c
N = int(input())
A, B, C = list(map(int, input().split()))

a = [0]+list(map(int,input().split()))
b = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))

print("a : " + str(a))
print("b : " + str(b))
print("c : " + str(c))

# 1 찾고
# 1 과 2와 위치가 다르면 +H(1)
# 2 와 3 과 위치가 다르면 +H(2) ...

answer = 0
before = 0
now = 0
if a[-1] == 1:
    before = 1
    del a[-1]
elif b[-1] == 1:
    before = 2
    del b[-1]
else :
    before = 3
    del c[-1]

for n in range(2, N):
    if a[-1] == n:
        now = 1
        del a[-1]
    elif b[-1] == n:
        now = 2
        del b[-1]
    else :
        now = 3
        del c[-1]

    if before == now:
        continue
    else:
        answer += (1<<n)-1
        before = now

if a[-1] == N:
    before = 1
    del a[-1]
elif b[-1] == N:
    before = 2
    del b[-1]
else :
    before = 3
    del c[-1]

print(before)
print(answer)

    