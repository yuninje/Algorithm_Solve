# https://www.acmicpc.net/problem/2748
# F(n) = F(n-1) + F(n-2) (n >= 2)

N = int(input())

fib = [0,1]

if(N >= 2):    
    for n in range(2,N+1):
        fib.append(fib[n-2] + fib[n-1])

print(fib[N])