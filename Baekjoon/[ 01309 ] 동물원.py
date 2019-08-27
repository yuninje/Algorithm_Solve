# https://www.acmicpc.net/problem/1309
# 1 <= N <= 100000

N = int(input())

a, b, c = 3, 7, 0
for d in range(2,N):
    c = ( a + 2 * b ) % 9901
    a,b = b,c
if N==1: print(a)
elif N==2 : print(b)
else: print(c)
