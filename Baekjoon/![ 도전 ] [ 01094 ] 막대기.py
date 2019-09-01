# https://www.acmicpc.net/problem/1094

X = int(input())
S = [64]
SUM = 64
while SUM != 64:
    if SUM - S[0] //2 == X:
        break
    else:
        SUM -= S[0]
        del S[0]

print(len(S))
