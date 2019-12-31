# https://www.acmicpc.net/problem/2023
# 1 <= N <= 8

def dfs(now, count):
    if count == N:
        print(now)
        return
    
    for n in range(1,10):
        if isPrime(now * 10 + n):
            dfs(now * 10 + n, count+1)

def isPrime(num):
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

N = int(input())
dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)