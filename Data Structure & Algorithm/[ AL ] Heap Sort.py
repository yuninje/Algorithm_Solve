def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def heap_add(heap, v):
    N = len(heap)
    
    heap.append(v)
    while N != 1 and v > heap[N//2]:
        swap(heap, N//2, N)
        N //= 2



arr = [1,3,4,2,5,7,6]
print('Heap Sort !')
print('before : ' + str(arr))
heap = []
for a in arr:
    heap_add(heap, a)
del heap[0]
print('after : ' + str(heap))