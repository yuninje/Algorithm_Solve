# https://www.acmicpc.net/problem/1094

N = int(input())
stick = 64
count = 1
while stick != N :
    stick //= 2

    if stick < N:
        N -= stick
        count += 1
    else:
        pass


print(count)