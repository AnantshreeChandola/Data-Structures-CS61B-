class MaxHeap:
    def __init__(self, l):
        self.l = l
        self.size = len(l)
        self.buildHeap()

    def heapifyBottomUp(self, idx): 
        if idx == None:
            return
        left = 2*idx + 1
        right = 2*idx + 2
        largest = None
        if left < self.size and self.l[left] > self.l[idx] and self.l[left] > self.l[right]:
            largest = left
        elif right < self.size and self.l[right] > self.l[left] and self.l[right] > self.l[idx]:
            largest = right
        if largest:
            self.l[largest], self.l[idx] = self.l[idx], self.l[largest]
            self.heapifyBottomUp(largest)

    def buildHeap(self):  #Ammortized time-complexity O(n) (only the non-leaf nodes are processed)
        last_non_leaf_node = self.size//2
        for index in range(last_non_leaf_node, -1, -1):
            self.heapifyBottomUp(index)

    def heapify(self): #O(log(n)) Bottom-up approach
        idx = self.size - 1
        parent = (idx-1)//2
        while parent >= 0 and self.l[parent] < self.l[idx]:
            self.l[parent], self.l[idx] = self.l[idx], self.l[parent]
            idx = parent
            parent = (idx-1)//2


    def heapPush(self, value): #O(log(n))
        self.l.append(value)
        self.size += 1
        self.heapify()

    def heapPop(self): #O(log(n))
        self.l[0], self.l[self.size-1] = self.l[self.size-1], self.l[0]
        popped_element = self.l.pop(-1)
        self.size -= 1
        self.heapifyBottomUp(0)
        return popped_element


    def getLevelOrderTraversal(self):
        return self.l

mh = MaxHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])
print(mh.getLevelOrderTraversal()) #[17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
mh.heapPush(92)
mh.heapPush(7)
print(mh.getLevelOrderTraversal()) #[92, 15, 17, 9, 6, 13, 10, 4, 8, 3, 1, 5, 7]
print(mh.heapPop()) #92
print(mh.getLevelOrderTraversal()) #[17, 15, 13, 9, 6, 7, 10, 4, 8, 3, 1, 5]

