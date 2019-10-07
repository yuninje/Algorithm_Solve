class Heap:
    heap = [0]
    size = 0
    def __init__(self):
        heap = [0]
        size = 0

    def push(self, x):
        self.heap.append(x)
        self.size += 1
        idx = self.size
        while idx > 1 and self.heap[idx//2] > self.heap[idx]:
            if self.heap[idx//2] < self.heap[idx]:
                break
            temp = self.heap[idx//2]
            self.heap[idx//2] = self.heap[idx]
            self.heap[idx] = temp
            idx //= 2
    
    def pop(self):
        pop = self.heap[1]
        self.heap[1] = self.heap[size]
        self.size -= 1
        idx = 1
        next = -1
        while True:
            next = idx * 2
            if next < self.size and self.heap[next] > self.heap[next+1]:
                next += 1
            if next > self.size or self.heap[next] > self.heap[idx]:
                break
            temp = self.heap[idx]
            self.heap[idx] = self.heap[next]
            self.heap[next] = temp
            idx = next
        return pop

heap = Heap()
for a in [1,5,2,4,6,8,3]:
    heap.push(a)



