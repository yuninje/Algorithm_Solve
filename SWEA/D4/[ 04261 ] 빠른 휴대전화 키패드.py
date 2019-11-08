T = int(input())
for test in range(1,T+1):
    S, N = input().split()
    N = int(N)
    arr = input().split()
    answer = 0

    counts = [0] * 10
    for s in S:
        counts[int(s)] += 1
    alpha = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

    ord_a = ord('a')
    for ar in arr:
        if len(ar) != len(S):
            continue
        counts_ = [0] * 10
        for a in ar:
            counts_[alpha[ord(a)-ord_a]] += 1

        for i in range(10):
            if counts[i] == counts_[i]:
                continue
            else:
                break
        else:
            answer += 1

    print('#' + str(test) + ' ' + str(answer))
