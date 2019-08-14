# https://www.acmicpc.net/problem/4375
# 1 <= N <= 10000

import sys
for line in sys.stdin:
    N = int(line)
    s = i = 1
    while s % N != 0:
        s = s*10+1
        i += 1
    print(i)


