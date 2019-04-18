class HashHeap:

    def __init__(self, desc=False):

        self.heap = []
        self.hash = dict()
        self.desc = desc 
        self.num_to_times = dict()

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

    def modify(self, num):

        if num not in self.num_to_times:

            self.num_to_times[num] = 1 
            self.push((1, num))

        else:

            item = (self.num_to_times[num], num)
            index = self.hash[item]

            del self.hash[item]

            self.num_to_times[num] += 1 
            self.heap[index] = (self.num_to_times[num], num)
            self.hash[(self.num_to_times[num], num)] = index 

            if index < self.size:

                self._sift_up(index)
                self._sift_down(index)

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

        while index * 2 + 1 < self.size:

            left = index * 2 + 1 
            right = index * 2 + 2 

            smallest = index 

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
        
class DataStream:

    def __init__(self):

        self.maxHeap = HashHeap(desc=True)

    def add(self, num):

        self.maxHeap.modify(num)

    def get_mode(self):

        return self.maxHeap.top()[1]

class Solution:

    def __init__(self, nums):

        self.nums = nums
        self.curt_nums = []
        self.ds = DataStream()

    def get_mode(self, nums):

        for num in nums:

            self.ds.add(num)

            self.curt_nums.append(num)

            print("currrnt nums: ", self.curt_nums)

            print("current mode: ", self.ds.get_mode())

            print("-" * 60)

solution = Solution([1, 2, 3, 4, 1, 5, 1, 2, 2, 2, 4, 6])

solution.get_mode(solution.nums)

