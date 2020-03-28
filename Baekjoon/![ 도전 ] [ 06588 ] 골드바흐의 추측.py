# https://www.acmicpc.net/problem/6588
import sys
I = sys.stdin.readline
arr = []
while True:
    arr.append(int(I().split()[0]))
    if arr[-1] == 0:
        break
MAX = max(arr)

prr = [ True ] * ( MAX + 1 )
prr[0], prr[1] = False, False
for i in range(2,MAX+1):
    if not prr[i]:
        continue
    j = i * 2
    while j < MAX+1:
        prr[j] = False
        j += i
    

nums = []
for i in range(MAX+1):
    if prr[i]:
        nums.append(i)
        

for a in arr:
    if a == 0:
        continue
    s = 0
    e = prr


