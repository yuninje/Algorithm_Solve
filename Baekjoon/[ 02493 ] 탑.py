# https://www.acmicpc.net/problem/2493

# N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 세우고.
# 탑의 꼭대기에 레이저 송신기 설치.

# 1 <= N <= 500,000
# 1 <= H <= 100,000,000
import sys
I = sys.stdin.readline
N = int(I())
arr = list(map(int, I().split()))
arr.insert(0,999999999)
result = [-1] * (N+1)
stack = [0]

for a in range(1,N+1):
    while arr[stack[-1]] <= arr[a]:
        stack.pop()      
    
    result[a] = stack[-1]
    stack.append(a)

del result[0]
print(' '.join(map(str,result)))
