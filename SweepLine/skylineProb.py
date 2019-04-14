class HashHeap:
    
    def __init__(self, desc=False):
        
        self.heap = [] 
        self.hash = dict()
        self.desc = desc 
        
    @property 
    def size(self):
        
        return len(self.heap)
        
    def push(self, item):
        
        self.heap.append(item)
        self.hash[item] = self.size - 1 
        
        self._sift_up(self.size - 1)
        
    def pop(self):
        
        item = self.heap[0]
        
        self.remove(item)
        
        return item 
        
    def top(self):
        
        return self.heap[0]
        
    def remove(self, item):
        
        if item not in self.hash:
            
            return 
        
        index = self.hash[item]
        self._swap(index, self.size - 1)
        
        del self.hash[item]
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
            
            self._swap(index, parent)
            index = parent 
            
    def _sift_down(self, index):
        
        if index is None:
            
            return 
        
        while index * 2  + 1 < self.size:
            
            smallest = index 
            
            left = index * 2 + 1 
            right = index * 2 + 2 
            
            if self._smaller(self.heap[left], self.heap[smallest]):
                
                smallest = left 
                
            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                
                smallest = right 
                
            if index == smallest:
                
                break 
            
            self._swap(index, smallest)
            index = smallest
            
    def _swap(self, i, j):
        
        item1 = self.heap[i]
        item2 = self.heap[j]
        
        self.heap[i] = item2 
        self.heap[j] = item1 
        
        self.hash[item1] = j 
        self.hash[item2] = i 
        
        
class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        
        points = [] 
        
        for index, (start, end, height) in enumerate(buildings):
            
            points.append((start, height, index, True))
            points.append((end, height, index, False))
            
        points = sorted(points)
        
        intervals = [] 
        last_position = None 
        
        max_heap = HashHeap(desc=True)
        
        for position, height, index, isStart in points:
            
            maxHeight = max_heap.top()[0] if max_heap.size else 0 
            
            self.merge_to(intervals, last_position, position, maxHeight)
            
            if isStart:
                
                max_heap.push((height, index))
                
            else:
                
                max_heap.remove((height, index))
                
            last_position = position 
            
        return intervals
        
    def merge_to(self, intervals, start, end, height):
        
        if start is None or height == 0 or start == end:
            
            return 
        
        if not intervals:
            
            intervals.append([start, end, height])
            
            return 
            
        _, prev_end, prev_height = intervals[-1]
        
        if prev_end == start and prev_height == height:
            
            intervals[-1][1] = end 
            
            return 
            
        intervals.append([start, end, height])