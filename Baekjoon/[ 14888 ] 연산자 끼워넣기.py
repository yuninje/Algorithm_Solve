# https://www.acmicpc.net/problem/14888
# 2 <= N <= 11
# 1 <= A <= 100

def dfs(total, count, plus, minus, multi, div):
    global max, min
    if plus < 0 or minus <0 or multi < 0 or div < 0:
        return

    if count == N-1:
        if total > max:
            max = total
        if total < min:
            min = total
        return

    dfs(total+arr[count+1], count+1, plus-1, minus, multi, div)
    dfs(total-arr[count+1], count+1, plus, minus-1, multi, div)
    dfs(total*arr[count+1], count+1, plus, minus, multi-1, div)
    if total < 0:
        dfs(((total * -1 ) // arr[count+1] )*-1, count+1, plus, minus, multi, div-1)
    else:
        dfs(total//arr[count+1], count+1, plus, minus, multi, div-1)


N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))


max = -9223372036854775808 # 가질 수 있는 최소값
min = 9223372036854775807  # 가질수 있는 최대값
dfs(arr[0], 0, oper[0], oper[1], oper[2], oper[3])

print(max)
print(min)