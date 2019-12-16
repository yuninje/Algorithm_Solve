# https://www.acmicpc.net/problem/1655
# 1 <= N <= 100,000
# -10000 <= arr[n] <= 10000 
import sys
I = sys.stdin.readline
def binary_search(start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if brr[mid] < value:
            start = mid + 1
        elif brr[mid] == value:
            return mid
        else:
            end = mid - 1
    return start
        

N = int(I())
arr = [int(I()) for _ in range(N)]
brr = [arr[0]]
print(brr[0])
for i in range(1,N):
    idx = binary_search(0,i-1,arr[i])
    brr.insert(idx, arr[i])
    print(brr[i//2])

# binary search 를 이용해 위치 찾기
# arr [ idx // 2 ] 출력
