# https://www.acmicpc.net/problem/1914
def Hanoi(start, end, height):
    if height == 1:
        print(str(start) + " " + str(end))
        return
    Hanoi(start, 6-start-end, height-1)
    print(str(start) + " " + str(end))
    Hanoi(6-start-end, end, height-1)

N = int(input())

print((1<<N)-1)
if N <= 20:
    Hanoi(1,3,N)