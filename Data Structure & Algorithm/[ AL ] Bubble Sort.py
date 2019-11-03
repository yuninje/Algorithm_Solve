def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

def bubble_sort(arr):
  N = len(arr)
  
  flag = True
  for i in range(N-1, -1, -1):
    if flag:
      flag = False  
      for j in range(i):
        if arr[j] > arr[j+1]:
          swap(arr, j+1, j)
          flag = True
    else:
      break
          
arr = [1,3,4,2,5,7,6]
print('Bubble Sort !')
print('before : ' + str(arr))
bubble_sort(arr)
print('after : ' + str(arr))