def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    
def selection_sort(arr):
    N = len(arr)
    
    for i in range(N):
        midx = i
        for j in range(i+1, N):
            if arr[midx] > arr[j]:
                midx = j
        swap(arr, i, midx)


arr = [1,3,4,2,5,7,6]
print('Selection Sort !')
print('before : ' + str(arr))
selection_sort(arr)
print('after : ' + str(arr))