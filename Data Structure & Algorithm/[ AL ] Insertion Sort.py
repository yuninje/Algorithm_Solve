def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def insertion_sort(arr):
    N = len(arr)
    
    for i_ in range(1,N):
        i = i_
        for j in range(i_-1, -1, -1):
            if arr[j] > arr[i]:
                swap(arr, i, j)
                i = j
            else:
                break

arr = [1,3,4,2,5,7,6]
print('Insertion Sort !')
print('before : ' + str(arr))
insertion_sort(arr)
print('after : ' + str(arr))