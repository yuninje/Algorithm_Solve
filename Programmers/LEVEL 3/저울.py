# 1 <= 저울추 <= 10000
# 1 <= 각 저울 추 <= 1000000

def solution(weight):
    weight = sorted(weight)
    total = 0
    for i in weight:
        if total < i:
            if i == total + 1:
                total += i
            else:
                return total+1
        else:
            total += i
    return total+1