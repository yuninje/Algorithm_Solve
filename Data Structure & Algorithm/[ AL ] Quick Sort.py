def quicksort2(arr,os, oe):
    if os >= oe:
        return
    print('=======================================')
    print(arr[os:oe+1])
    p = oe

    s = os
    e = oe-1

    while s < e:

        while arr[s] < arr[p] and s < e:
            s += 1
        while arr[e] > arr[p] and s < e :
            e -= 1

        swap(arr,s,e)
        print(arr)
    if arr[s] <= arr[p]:
        swap(arr,s+1,p)
        quicksort2(arr,os,s)
        quicksort2(arr,s+2,oe)
    elif arr[s] > arr[p]:
        swap(arr,s,p)
        quicksort2(arr,os,s-1)
        quicksort2(arr,s+1,oe)

def quicksort1(arr, s, e):
    if e - s == 0 or e - s == 1:
        return
    p = s
    l = s + 1
    r = e-1
    while True:
        while True:
            if l <= e -1 and arr[p] > arr[l]:
                l += 1
            else:
                break
        
        while True:
            if r > s and arr[p] < arr[r]:
                r -= 1
            else:
                break
            
        if l < r:
            swap(arr,l,r)
        else:
            swap(arr,p,r)
            break
    quicksort1(arr, s, r)
    quicksort1(arr, r+1, e)

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


brr = [7, 5, 1, 8, 4, 0, 8, 10, 9, 2, 14, 6, 5, 3, 6]
quicksort1(brr,0,len(brr))

arr = [7, 5, 1, 8, 4, 0, 8, 10, 9, 2, 14, 6, 5, 3, 6]
quicksort2(arr,0,len(arr)-1)
