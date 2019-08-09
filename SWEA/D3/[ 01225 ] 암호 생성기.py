for t in range(0,10):
    test = int(input())
    arr = list(map(int, input().split()))
    idx = 0
    count = 1
    while True:
        arr[idx] -= count
        if arr[idx] <= 0:
            arr[idx] = 0
            break
        idx = (idx +1) % 8

        count = count % 5 + 1

    result = arr[idx+1:] + arr[:idx+1]

    print("#" + str(test) + " " + str(result)[1:-1].replace(',', ''))