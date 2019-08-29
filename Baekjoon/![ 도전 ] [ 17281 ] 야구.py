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

def move_ru(count):
    global ru
    global score
    flag = False

    while(count!= 0):
        for i in range(0,3):
            ru[i] = ru[i+1]
        if ru[0]:
            ru[0] = False
            score += 1
        ru[3] = False
        if not flag:
            flag = True
            ru[3] = True
        count -= 1

N = int(input())
inning = [list(map(int, input().split())) for _ in range(0,N)]
lists = []
perm = []
visit = [False] * 9
find(0)
# lists = [[4,5,6,0,1,2,3,7,8]]
ru = [False, False, False, False]
MAX = 0

for l in lists:
    idx = -1
    score = 0
    inn = 0
    while inn != N:
        for i in range(0,4):
            ru[i] = False         
        out = 0
        while out != 3:
            idx = (idx +1) % 9
            man = l[idx]
            if inning[inn][man] == 0:
                out += 1
            else:
                move_ru(inning[inn][man])
                # score += 1
        inn += 1
    if MAX < score:
        MAX = score
print(MAX)