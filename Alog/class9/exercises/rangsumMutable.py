class SegmentNode(object):
    
    def __init__(self, start, end, val):
        
        self.start = start
        self.end = end 
        self.val = val 
        self.left = None 
        self.right = None 
        
class SegmentTree(object):
    
    def __init__(self, A):
        
        self.root = self.build(A)
        
    def build(self, A):
        
        return self.build_helper(0, len(A) - 1, A)
        
    def build_helper(self, start, end, A):
        
        if start > end:
            
            return None 
            
        if start == end:
            
            return SegmentNode(start, end, A[start])
            
        node = SegmentNode(start, end, 0)
        
        mid = (start + end) // 2 
        
        node.left = self.build_helper(start, mid, A)
        
        node.right = self.build_helper(mid + 1, end, A)
        
        if node.left:
            
            node.val += node.left.val 
            
        if node.right:
            
            node.val += node.right.val 
            
        return node 
        
    def modify(self, root, index, value):
        
        if root.start == root.end and root.start == index:
            
            root.val = value 
            
            return 
        
        mid = (root.start + root.end) // 2 
        
        if index <= mid:
            
            self.modify(root.left, index, value)
            
            root.val = root.left.val + root.right.val
            
        else:
            
            self.modify(root.right, index, value)
            
            root.val = root.left.val + root.right.val 
            
        return 
        
    def query(self, root, start, end):
        
        if start <= root.start and root.end <= end:
            
            return root.val 
            
        if start > root.end or end < root.start:
            
            return 0
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)
            

class BinaryIndexTree(object):
    
    def __init__(self, A):
        
        self.A = A 
        self.C = [0] * (len(A) + 1) 
        self.n = len(A)
        
        for i in range(0, self.n):
            
            self.add(i, A[i])
        
    def add(self, idx, val):
        
        idx += 1
        while idx <= self.n:
            self.C[idx] += val
            idx += self.lowbit(idx)
            
    def lowbit(self, x):
        
        return x & -x
        
    def range_sum(self, idx):
        
        idx += 1
        res = 0
        while idx > 0:
            res += self.C[idx]
            idx -= self.lowbit(idx)
        return res
     
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #
        # Solution1: SegmentTree
        #
        
        # self.tree = SegmentTree(nums)
        
        # self.root = self.tree.root 
        
        #
        # Solution2: Binary Index Tree
        #
        
        self.bit = BinaryIndexTree(nums)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        #
        # Solution1: SegmentTree
        #
        
        # self.tree.modify(self.root, i, val)
        
        #
        # Solution2: Binary Index Tree
        #
        self.bit.add(i, val - self.bit.A[i])
        self.bit.A[i] = val 
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #
        # Solution1: SegmentTree
        #
        
        # return self.tree.query(self.root, i, j)
        
        #
        # Solution2: Binary Index Tree
        #
        
        return self.bit.range_sum(j) - self.bit.range_sum(i - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)