# https://www.acmicpc.net/problem/1920
# N(1≤N≤100,000)
# M(1≤M≤100,000)

N = int(input())
nrr = list(map(int, input().split()))
M = int(input())
mrr = list(map(int, input().split()))

nrr = sorted(nrr)
for m in mrr:
    start = 0
    end = N-1
    while(True):
        middle = (start + end) // 2
        if nrr[middle] < m:
            start = middle+1
        elif nrr[middle] > m:
            end = middle-1
        else:
            print(1)
            break
        if end < start:
            print(0)
            break

# set 이용.========================================================
# set에서는 Hash 를 통해서 자료를 저장하기 때문에 시간 복잡도가 O(1)
# N = int(input())
# nrr = set(map(int, input().split()))
# M = int(input())
# mrr = list(map(int, input().split()))

# for m in mrr:
#     if m in nrr:
#         print(1)
#     else:
#         print(0)
