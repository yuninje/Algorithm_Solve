def quick_sort(start, end):
    if end - start == 0 or end - start == 1:
        return
    pivot = start
    l = start + 1
    r = end-1
    while True:
        while True:
            if l <= end -1 and arr[pivot] > arr[l]:
                l += 1
            else:
                break
        
        while True:
            if r > start and arr[pivot] < arr[r]:
                r -= 1
            else:
                break
            
        if l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
        else:
            temp = arr[pivot]
            arr[pivot] = arr[r]
            arr[r] = temp
            break
    quick_sort(start, r)
    quick_sort(r+1, end)

arr = [3,2,1,4,5,8,6,0]
print(arr)
quick_sort(0, len(arr))
print(arr)



    