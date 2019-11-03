def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def merge_sort(arr, si, ei):
    if si == ei-1:
        return [arr[si]]
    mi = (si + ei) // 2

    # Devide
    left = merge_sort(arr, si, mi)
    right = merge_sort(arr, mi, ei)

    li = 0
    li_max = mi - si
    ri = 0
    ri_max = ei - mi
    result = []
    
    # Combine
    while li != li_max and ri != ri_max:
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1
    for i in range(li,li_max):
        result.append(left[i])
    for i in range(ri,ri_max):
        result.append(right[i])

    return result

arr = [1,3,4,2,5,7,6]
print('Merge Sort !')
print('before : ' + str(arr))
result = merge_sort(arr, 0, len(arr))
print('after : ' + str(result))