# https://www.acmicpc.net/problem/2023
# 1 <= N <= 8

def bfs():
    count = 1
    
    queue = [2,3,5,7]
    while queue:
        queue_ = []
        if count == N:
            for q in queue:
                print(q)
            return
        for q in queue:
            for i in range(1,10):
                a = q*10+i
                if isPrime(a):
                    queue_.append(a)
        queue = queue_
        count += 1

def isPrime(a):
    for i in range(2,a//2+1):
        if a % i == 0:
            return False
    return True

N = int(input())
# arr = [True] * (10**N)
# for i in range(2,len(arr)):
#     if arr[i]:
#         x = i+i
#         while x < len(arr):
#             arr[x] = False
#             x += i
bfs()