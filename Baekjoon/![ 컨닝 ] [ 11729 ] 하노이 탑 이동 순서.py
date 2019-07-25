def move(start, end, count):
    if count == 1:
        print(str(start) + " " + str(end))
        return
    move(start, 6-start-end, count-1)
    print(str(start) + " " + str(end))
    move(6-start-end, end, count-1)


N = int(input())
print((1<<N) -1)
move(1,3,N)