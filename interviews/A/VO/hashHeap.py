class HashHeap:

    def __init__(self, desc=False):

        self.heap = [] 
        self.item_to_index = {} 
        self.desc = desc  

    @property 
    def size(self):
        return len(self.heap)

    def push(self, item): 

        self.heap.append(item)

        self.item_to_index[item]

        self._sift_up(self.size - 1)

    def pop(self): 

        item = self.heap[0]

        self.remove(item)

        return item 

    def top(self):

        return self.heap[0] 

    def remove(self, item):

        if item not in self.item_to_index:
            return 

        idx = self.item_to_index[item] 
        self._swap(idx, self.size - 1)

        self.heap.pop()
        del self.item_to_index[item]

        if idx < self.size: 
            self._sift_up(idx)
            self._sift_down(idx) 

    def _smaller(self, left, right):

        return left > right if self.desc else left < right 

    def _sift_up(self, index):

        while index != 0:

            parent = (index - 1) // 2 

            if self._smaller(self.heap[parent], self.heap[index]):
                break 

            self._swap(index, parent)
            index = parent 

    def _sift_down(self, index):

        while index * 2 + 1 < self.size: 

            left = index * 2 + 1 
            right = index * 2 + 2 

            smallest = index 

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left 

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right 

            if smallest == index:
                break 

            self._swap(index, smallest)
            index = smallest 

    def _swap(self, index1, index2):

        item1 = self.heap[index1]
        item2 = self.heap[index2]

        self.heap[index1] = item2
        self.heap[index2] = item1 

        self.item_to_index[item1] = index2 
        self.item_to_index[item2] = index1 
        

    