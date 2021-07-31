class MinHeap:
    heap = []
    #If the elements are not dynamically inserted, we can perform the heapify operation with O(n) complexity by using botton-up heapify
    #on non-leaf nodes.
    #top-down heapify to build heap
    def heapifytopdown(self, key):
        current = len(self.heap)-1
        while(((current-1)//2 >= 0) and self.heap[(current-1)//2] > key):
            self.heap[current], self.heap[(current-1)//2] = self.heap[(current-1)//2], self.heap[current]
            current = (current-1)//2
    #bottom-up heapify
    def heapifyroot(self):
        current = 0
        length = len(self.heap)
        while((current*2 + 2) < length and (min(self.heap[current*2+1], self.heap[current*2+2]) < self.heap[current])):
            exchange = (current*2 + 1) if (self.heap[current*2+1] < self.heap[current*2+2]) else (current*2+2)
            self.heap[exchange], self.heap[current] = self.heap[current], self.heap[exchange]
            current = exchange
    def Add(self, key):
        self.heap.append(key)
        self.heapifytopdown(key)
    def GetSmallest(self):
        return self.heap[0]
    def RemoveSmallest(self):
        length = len(self.heap)
        self.heap[0], self.heap[length-1] = self.heap[length-1], self.heap[0]
        del self.heap[length-1]
        self.heapifyroot()
    def GetSize(self):
        return len(self.heap)
pq = MinHeap()
pq.Add(1)
pq.Add(2)
pq.Add(3)
pq.Add(0)
pq.Add(9)
pq.Add(4)
pq.Add(5)
print(pq.heap)
print(pq.GetSmallest())
pq.RemoveSmallest()
print(pq.heap)
print(pq.GetSize())

