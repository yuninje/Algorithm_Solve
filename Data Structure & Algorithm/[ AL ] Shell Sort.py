def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def shell_sort(arr):
    dist = len(arr) // 2
    while dist < 1:
        for i in range(dist):
            

arr = [1,3,4,2,5,7,6]
print('Shell Sort !')
print('before : ' + str(arr))
shell_sort(arr)
print('after : ' + str(arr))