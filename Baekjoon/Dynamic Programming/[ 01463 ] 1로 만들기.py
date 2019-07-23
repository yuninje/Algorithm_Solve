def dfs_iterative(N):
    list_ = []
    if N % 3 == 0:
        list_.append(arr[int(N/3)]+1)
    if N % 2 == 0:
        list_.append(arr[int(N/2)]+1)
    list_.append(arr[N-1] + 1)

    return min(list_)


N = int(input())
arr = [int(0) for _ in range(0,N+1)]
arr[1] = int(0)
for i in range (2, N+1):
    arr[i] = dfs_iterative(i)

print(arr[N])