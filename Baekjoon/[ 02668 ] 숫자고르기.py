# https://www.acmicpc.net/problem/2668
# 1 <= N <= 100

N = int(input())
arr = [0]
for n in range(0,N):
    arr.append(int(input()))
    
# inner = [[0] * (N+1) for _ in range(0,N+1)]

# for i in range(1,N+1):
#     inner[arr[i]][i] = 1

longList = []
visit = [False] * (N+1)
l = []
for i in range(1,N+1):
    if visit[i]:
        continue 
    visit[i] = True
    if i == arr[i]:
        longList.append(i)
    else:
        if not visit[arr[i]]:
            visit[arr[i]] = True
            li = [i, arr[i]]
            while not arr[li[-1]] in li:
                li.append(arr[li[-1]])
                visit[li[-1]] = True
                if visit[arr[li[-1]]]:
                    break

            for l in range(0,len(li)):
                if li[l] == arr[li[-1]]:
                    temp = li[l:]
                    longList += temp
print(len(longList))
for l in sorted(longList):
    print(l)