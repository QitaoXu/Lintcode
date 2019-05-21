class HashHeap:
    
    def __init__(self, desc = False):
        
        self.heap = [] 
        self.item_to_index = {} 
        self.desc = desc 
        
    @property 
    def size(self):
        
        return len(self.heap)
        
    def push(self, item):
        
        self.heap.append(item)
        self.item_to_index[item] = self.size - 1 
        
        self._sift_up(self.size - 1)
        
    def pop(self):
        
        item = self.heap[0]
        
        self.remove(item)
        
        return item 
        
    def top(self):
        
        return self.heap[0]
        
    def remove(self, item):
        
        if item not in self.heap:
            
            return 
        
        index = self.item_to_index[item]
        self._swap(index, self.size - 1)
        
        del self.item_to_index[item]
        self.heap.pop()
        
        if index < self.size:
            
            self._sift_up(index)
            self._sift_down(index)
            
    def _smaller(self, left, right):
        
        return right < left if self.desc else left < right 
        
    def _sift_up(self, index):
        
        while index != 0:
            
            parent = (index - 1) // 2
            
            if self._smaller(self.heap[parent], self.heap[index]):
                
                break 
            
            self._swap(parent, index) 
            index = parent
            
    def _sift_down(self, index):
        
        if index is None:
            
            return 
        
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
            
            self._swap(smallest, index)
            index = smallest
            
    def _swap(self, i, j):
        
        item1 = self.heap[i]
        item2 = self.heap[j]
        
        self.heap[j] = item1 
        self.heap[i] = item2 
        
        self.item_to_index[item1] = j 
        self.item_to_index[item2] = i 


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        
        if not nums or len(nums) < k:
            
            return [] 
            
        self.maxHeap = HashHeap(desc = True)
        self.minHeap = HashHeap()
        
        for i in range(k - 1):
            
            self.add((nums[i], i))
            
        medians = [] 
        
        for i in range(k - 1, len(nums)):
            
            self.add((nums[i], i))
            
            medians.append(self.median)
            
            self.remove((nums[i - k + 1], i - k + 1))
            
        return medians 
        
    def add(self, item):
        
        if self.maxHeap.size > self.minHeap.size:
            
            self.minHeap.push(item)
            
        else:
            
            self.maxHeap.push(item)
            
        if self.maxHeap.size == 0 or self.minHeap.size == 0:
            
            return 
        
        if self.maxHeap.top() > self.minHeap.top():
            
            self.maxHeap.push(self.minHeap.pop())
            self.minHeap.push(self.maxHeap.pop())
            
    def remove(self, item):
        
        self.maxHeap.remove(item)
        self.minHeap.remove(item)
        
        if self.maxHeap.size < self.minHeap.size:
            
            self.maxHeap.push(self.minHeap.pop())
            
    @property
    def median(self):
        
        return self.maxHeap.top()[0]
