# https://www.acmicpc.net/problem/17281
# 2 <= N <= 50
import sys
sys.setrecursionlimit(10 ** 6)

def find(count):
    global perm
    if count == 9:
        lists.append(perm[:])
        return
    if count == 3:
        visit[0] = True
        perm.append(0)
        find(4)
        del perm[-1]
        visit[0] = False
        return
    for i in range(1,9):
        if visit[i]:
            continue
        visit[i] = True
        perm.append(i)
        find(count+1)
        del perm[-1]
        visit[i] = False
