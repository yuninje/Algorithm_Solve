def bubble_sort(arr):
  for j in range(0, len(arr)):
    for i in range(0, len(arr)-1 -j):
      if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
  
  return arr

arr = [1,3,4,2,5,7,6]
print(arr)
print(bubble_sort(arr))
