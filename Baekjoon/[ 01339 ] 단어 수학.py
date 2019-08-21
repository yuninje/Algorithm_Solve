# https://www.acmicpc.net/problem/1339
# 1 <= N <= 10
# 1 <= arr[n] <= 8

N = int(input())
arr = [0] * 26
for n in range(0,N):
    line = input()
    for l in range(0,len(line)):
        arr[ord(line[l])-ord('A')] += 10**(len(line)-1-l)

arr = sorted(arr, reverse=True)
result = 0
for i in range(0,10):
    result += arr[i] * (9-i)

print(result)