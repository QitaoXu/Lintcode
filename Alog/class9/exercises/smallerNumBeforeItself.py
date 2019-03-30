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
            
            root.val += value 
            
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

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        
        if len(A) == 0:
            return []
        
        tree = SegmentTree( [0] * (max(A) + 1) )
        root  = tree.root 
        
        results = []
        
        for i in range(len(A)):
            
            range_sum = tree.query(root, 0, A[i] - 1)
            
            results.append(range_sum)
            
            tree.modify(root, A[i], 1)
            
        return results