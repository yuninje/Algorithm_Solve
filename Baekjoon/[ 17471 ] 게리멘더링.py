# https://www.acmicpc.net/problem/17471
# 2 <= N <= 10
# 1 <= arr[n] <= 100

import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline

def make_group(count):
    global groupA
    global groupB
    global answer

    if count == N:
        # 체크
        if check():
            answer = min(answer, cal_group())
            # 계산
        return

    groupA.append(count)
    make_group(count+1)
    del groupA[-1]

    groupB.append(count)
    make_group(count+1)
    del groupB[-1]

def check():
    if len(groupA) == 0 or len(groupB) == 0:
        return False

    visit = [False] * N

    dfs(groupA[0], groupA, visit)
    dfs(groupB[0], groupB, visit)

    for i in range(N):
        if not visit[i]:
            return False
    return True

def dfs(g, group, visit):
    visit[g] = True
    for i in groups[g]:
        if visit[i]:
            continue
        if i in group:
            dfs(i, group, visit)

def cal_group():
    totalA = 0
    totalB = 0
    for a in groupA:
        totalA += arr[a]
    for b in groupB:
        totalB += arr[b]
    
    return abs(totalA-totalB)

N = int(I())
arr = list(map(int, I().split()))
groups = []
for _ in range(N):
    list_ = list(map(lambda x : int(x)-1, I().split()))
    del list_[0]
    groups.append(list_)
# for g in range(len(groups)):
#     print(str(g) + " : " + str(groups[g]))
groupA = []
groupB = []
answer = 999999999

# 그룹 만들기
make_group(0)

if(answer == 999999999):
    answer = -1
print(answer)